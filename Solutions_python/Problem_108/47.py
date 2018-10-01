#!/usr/bin/env python
import math, sys

def solve(t):
  N = int(input.readline())
  ds = []
  ls = []
  for i in xrange(N):
    d, l = map(int, input.readline().split())
    ds.append(d)
    ls.append(l)
  D = int(input.readline())
  ms = [None for _ in xrange(N)]
  ms[0] = ds[0]

  for i in xrange(0, N):
    if ms[i] is None:
      continue
    for j in xrange(i+1, N):
      if ds[j] > ds[i] + ms[i]:
        break
      m = ms[j]
      nm = min(ls[j], ds[j] - ds[i])
      if m is None or m < nm:
        ms[j] = nm
  best = 0
  for i in xrange(N):
    if ms[i] is None:
      continue
    best = max(ds[i] + ms[i], best)
  print >>output, 'Case #%d:' % t, 'YES' if best >= D else 'NO'

test = 'A-large'
input = open('%s.in'%test)
output = open('%s.out'%test, 'w')
#output = sys.stdout

for t in xrange(1, int(input.readline())+1):
  solve(t)
