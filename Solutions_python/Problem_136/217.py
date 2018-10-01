#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint


def solveCase(k, c, f, x):
  t = 0

  while True:
    tx = x / k

    tc = c / k
    k2 = k + f
    tcx = tc + (x / k2)
    if tx <= tcx:
      return t + tx
    k = k2
    t = t + tc

def solve(s):
  t = int(s.readline())

  for i in range(t):
    c, f, x = [float(f) for f in s.readline().split()]
    print('Case ' + str(i + 1))
    r = solveCase(2.0, c, f, x)
    yield str(r)

def main(argv=None):
  fileName = argv[1]
  s = open(fileName)
  r = open(fileName + '.result.txt'  , 'w')

  result = solve(s)
  for i, case in enumerate(result, 1):
    r.write('Case #' + str(i) + ': ' + case + '\n')
        
  return 0

if __name__ == '__main__':
  status = main(sys.argv)
  sys.exit(status)
