#!/usr/bin/env python
from collections import deque
def rec(A, B):
  PAIRS = set()
  for i in xrange(A+1, B+1):
    si = str(i)
    n = len(si)
    d = deque(si)
    for j in xrange(n-1):
      d.rotate(1)
      x = int(''.join(d))
      sx = str(x)
      if len(sx) == n and si != sx and x >= A and x <= B and (sx+'#'+si) not in PAIRS:
        PAIRS.add(si+'#'+sx)
  return len(PAIRS)

import sys
f=open(sys.argv[1])
L = f.read().split('\n')[1:]
L.pop()
for i, line in enumerate(L):
  nums = line.split(' ')
  print "Case #%s: %s" % (i+1, rec(int(nums[0]), int(nums[1])))
