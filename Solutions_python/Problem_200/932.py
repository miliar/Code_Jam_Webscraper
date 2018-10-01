def parseInputFrom(line):
  return line.strip()

def solve(k):
  if k == "":
    return k
  rep = [int(x) for x in k]
  for i in range(len(rep) - 1):
    if rep[i+1] < rep[i]:
      return str(int(solve(str(int(k) // 10 - 1)) + "9"))
  return k

def represent(i, res):
  return "Case #"+str(i)+": "+("IMPOSSIBLE" if res is None else str(res))

with open("input.in") as f:
  with open("output.out", "w") as f2:
    n = int(f.readline())
    i = 1
    line = f.readline()
    while line and i <= n:
      print(i, "/", n)
      k = parseInputFrom(line)
      res = solve(k)
      f2.write(represent(i, res)+"\n")
      i += 1
      line = f.readline()
