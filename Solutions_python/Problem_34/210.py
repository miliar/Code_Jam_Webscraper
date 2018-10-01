#!/usr/bin/python
import sys
from sets import Set


f = sys.stdin
s = f.readline().split()
L, D, N = int(s[0]), int(s[1]), int(s[2])

d = []
for i in xrange(0, D):
  d.append(f.readline())

for i in xrange(0, N):
  s = f.readline()
  p = []
  j = 0
  while j < len(s):
    if s[j] == '(':
      j = j + 1
      p.append(Set())
      while s[j] != ')':
        p[-1].add(s[j])
        j = j + 1
    else:
      p.append(Set(s[j]))
    j = j + 1
  cnt = 0
  for s in d:
    match = True
    for j in xrange(0, L):
      if s[j] not in p[j]:
        match = False
        break
    if match:
      cnt = cnt + 1
  print 'Case #'+str(i+1)+':', cnt

