import sys
sys.setrecursionlimit(1500)

def func(S, count, index, engines, queries):
  dist = []
  for ch in S:
    try:
      dist.append(queries[index:].index(ch) + index)
    except ValueError:
      return count
  newS = list(engines)
  newS.remove(S[dist.index(max(dist))])
  try:
    return func(newS, count + 1, max(dist), engines, queries)
  except:
    print max(dist)
    return count

def countSwitch(engines, queries):
  count = 0
  while True:
    rows = []
    permutation(engines, [], 0, engines, rows, count + 1)
    for row in rows:
      index = 0
      for engine in row:
        index = when(engine, queries, index)
      if index == -1:
        return count
    count += 1

def permutation(S, T, num, engine, result, r):
  if num == r:
    result.append(T)
  else:
    for ch in S:
      newS = list(engine)
      newS.remove(ch)
      newT = list(T)
      newT.append(ch)
      permutation(newS, newT, num + 1, engine, result, r)

def when(engine, queries, index):
  for i in range(len(queries[index:])):
    if queries[i + index] == engine:
      return i + index
  return -1

fin = open("input.txt", "r")
fout = open("output.txt", "w")
case = int(fin.readline())
for i in range(case):
  engines = []
  queries = []
  e = int(fin.readline())
  for j in range(e):
    engines.append(fin.readline()[:-1])
  q = int(fin.readline())
  for j in range(q):
    queries.append(fin.readline()[:-1])
  fout.write("Case #%d: %d\n" % (i+1, func(engines, 0, 0, engines, queries)))

fin.close()
fout.close()
