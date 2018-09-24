import sys

dparray = None
engines = None
queries = None
s = None
q = None

def rundp(qnum, snum):
  global dparray, engines, queries, s, q
  if qnum == q:
    return 0
  if dparray[qnum][snum] != None:
    return dparray[qnum][snum]
  
  try:
    runningIdx = engines.index(queries[qnum])
  except:
    runningIdx = -1

  best = q + 1
  for i in range(s):
    if i == runningIdx: #If this is the one about to run, we can't use it
      continue
    num = rundp(qnum+1, i) #Find out the number of switches if we go to this
    if i != snum: # If it's a switch, add one
      num += 1
    if num < best:
      best = num

  dparray[qnum][snum] = best
  return best

def main():
  global dparray, engines, queries, s, q
  sys.setrecursionlimit(10000)
  nc = int(raw_input())
  for c in range(1,nc+1):
    # Get engines
    s = int(raw_input())
    engines = [0]*s
    for i in range(s):
      engines[i] = raw_input()

    # Get queries
    q = int(raw_input())
    queries = [0]*q
    for i in range(q):
      queries[i] = raw_input()

    dparray = [None]*q
    for i in range(q):
      dparray[i] = [None]*s

    best = q+1
    for i in range(s):
      num = rundp(0,i)
      if num < best:
        best = num

    print "Case #%d: %d" % (c,best)

if __name__ == "__main__":
  main()
