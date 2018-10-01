import fileinput
input = fileinput.input()


def dumpSet(s,e,sums):
  print ("{0}".format(s-e),end="")
  s = e; e = sums[e]
  while s > 0:
    print(" {0}".format(s-e),end="")
    s = e; e = sums[e]
  print()

T = int(input.readline())

for t in range(1,T+1):
  line = input.readline().split(' ')
  N = int(line[0]); line = line[1:]
  S = list(map(int, line))

  maximum = sum(S)/2
  sums = {0:0}
  found = None

  for s in S:
    newsums = {}
    for e in sums.keys():
      if s+e <= maximum:
        newsums[s+e] = e
        if s+e in sums:
          found = (s+e, e, sums[s+e])
          break
    sums.update(newsums)
    if found is not None:
      break

  print ("Case #{0}:".format(t))
  if found is not None:
    dumpSet(found[0],found[1],sums)
    dumpSet(found[0],found[2],sums)
  else:
    print ("Impossible")
