#!/usr/bin/env python

import operator

bits = [2**n for n in range(20, -1, -1)]

def solve(cs):
  m = 0
  cs.sort()
  left = cs[:1]
  right = cs[1:]
  if reduce(operator.xor, left) == reduce(operator.xor, right):
    print sum(right)
  else:
    print 'NO'

if __name__ == "__main__":
  import sys
  inputFile = file(sys.argv[1], 'r')
  T = int(inputFile.readline())

  for i in range(0, T):
    sys.stdout.write('Case #%d: ' % (i+1))
    N = int(inputFile.readline())
    cs = [int(c) for c in inputFile.readline().split()]
    solve(cs)
  
  inputFile.close()
