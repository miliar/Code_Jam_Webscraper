#!/usr/bin/env python

import sys

def get_possible_best(ti):
  if ti == 0:     return (0,       0)
  ti3 = ti // 3
  if ti % 3 == 0: return (ti3,     ti3 + 1)
  if ti % 3 == 1: return (ti3 + 1, ti3 + 1)
  if ti % 3 == 2: return (ti3 + 1, ti3 + 2)

nl = int(sys.stdin.readline())

for i in range(nl):
  l = sys.stdin.readline().rstrip('\n').split(' ', 3)
  S = int(l[1])
  p = int(l[2])
  t = l[3].split(' ')

  b = bs = 0
  for ti in t:
    n1, n2 = get_possible_best(int(ti))
    if n1 >= p:
      b  += 1
    else:
      if n2 >= p:
        bs += 1
  print("Case #%d: %d" % (i + 1, b + min(bs,S)))
