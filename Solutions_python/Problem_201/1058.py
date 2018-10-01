from time import time
import heapq
import math

inp = open('c.in', 'r+')
out = open('c.out', 'w')

T = int(inp.readline())

for t in range(T):
  s = inp.readline().strip().split(" ")
  n = int(s[0])
  k = int(s[1])

  counts = {n:1}
  reductions = 0

  while reductions < k:
    vals = counts.keys()
    vals.sort()
    v = vals[-1]
    c = counts[v]

    replicates = min(c, n - reductions)
    reductions += replicates

    nv1 = int(math.floor((v-1)/2.0))
    nv2 = int(math.ceil((v-1)/2.0))
    if nv1 not in counts:
      counts[nv1] = 0
    counts[nv1] += replicates
    if nv2 not in counts:
      counts[nv2] = 0
    counts[nv2] += replicates

    counts[v] -= replicates
    if counts[v] == 0:
      del counts[v]

  o = str(nv2) + " " + str(nv1)

  out.write("Case #"+str(t+1)+": "+o+"\n")

out.close()