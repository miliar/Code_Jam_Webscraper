import os, sys

with open("in.txt") as f:
  lines = [x.strip() for x in f.readlines()]

cnt = int(lines[0])
for t in range(cnt):
  num = t + 1
  row = lines[num].split()
  cakes = [0 if x == '-' else 1 for x in row[0]]
  K = int(row[1])
  flips = 0
  L = len(cakes)
  for i in range(L - K + 1):
    if cakes[i] == 0:
      flips += 1
      for j in range(K,):
        cakes[i + j] ^= 1
  impossible = False
  for i in range(L - K + 1, L):
    if cakes[i] == 0:
      impossible = True
      break
  if impossible:
    print("Case #%d: IMPOSSIBLE" % (num))
  else:
    print("Case #%d: %d" % (num, flips))
  