#!/usr/bin/env python2.6

import itertools
import sys

def xor_sum(l):
  val = 0
  for i in l:
    val = val^i
  return val

def solve(n,l):
  result = 0
  for i in range(1,n/2+1):
    for comb in itertools.combinations(l,i):
      lcomb = list(l)
      for num in comb:
        lcomb.remove(num)
      if xor_sum(comb)==xor_sum(lcomb):
        result = max(result, max(sum(comb),sum(lcomb)))

  return str(result or 'NO')

T = 0
Ti = 0
n = 0
l = []

for line in sys.stdin:
  if Ti == 0:
    T = int(line.strip())
    Ti = 1
  elif not n: n = int(line.strip())
  elif not l:
    l = [int(j) for j in line.strip().split(' ')]
    print 'Case #%d: %s' % (Ti, solve(n,l))
    n = 0
    l = []
    Ti += 1
  if Ti>T: break
