#!/usr/bin/python

import sys
import math

try:
  import psyco
  psyco.full()
except Exception, e:
  pass

###

def solve(trees):
  count = 0

  a = []
  for i in trees:
    a.append(i)

  for i in xrange(len(trees)):
    for j in xrange(i + 1, len(trees)):
      for k in xrange(j + 1, len(trees)):
         x = (a[i][0] + a[j][0] + a[k][0]) / 3.0
         y = (a[i][1] + a[j][1] + a[k][1]) / 3.0
         if (x, y) == (math.floor(x), math.floor(y)):
           count += 1

  print count
###

if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  NTEST =  int(f.readline())
  for i in xrange(NTEST):
    print ('Case #%d:' % (i + 1)),
    n, A, B, C, D, x0, y0, M  = map(int, f.readline().strip().split())
    X = x0
    Y = y0
    TREE = set()
    TREE.add((X, Y))
    for i in xrange(1,  n):
      X = (A * X + B) % M
      Y = (C * Y + D) % M
      TREE.add((X, Y))
    solve(TREE)


    #int(f.readline())
