import os
import math

def solve(D, N, horses):
  maxtime = 0
  for K, S in horses:
    time = float(D - K) / S
    maxtime = max(maxtime, time)
  minspeed = float(D) / maxtime
  return minspeed

fin = open('A-large (1).in', 'r')
fout = open('A.out', 'w')
nown = 0
nowt = 0
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  line = line.strip()
  if nown == 0:
    D, N = line.split()
    N = int(N)
    D = int(D)
    horses = []
    nown = N
    nowt += 1
  else:
    nown -= 1
    K, S = line.split()
    K = int(K)
    S = int(S)
    horses.append((K, S))

  if nown == 0:
    res = solve(D, N, horses)

    out_str = 'Case #%d: %s\n' % (nowt, res)
    print out_str
    fout.write(out_str)
fin.close()
fout.close()
