#!/usr/bin/env python

import sys

def do_case(f):
  info = [int(x) for x in f.readline().split()]
  n = info[0]
  m = info[1]
  pair_hash = {}
  for x in range(n,m):
    y = str(x)
    #print y
    for d in range(len(y)-1):
      y = y[-1:] + y[:-1]
      #print "subcase: %s" % (y)
      if x < int(y) and (int(y) <= m):
        pair_hash[str(x) + '_' + y] = 1
    #print added
  return len(pair_hash)

f = sys.stdin
T = int(f.readline())
for i in xrange(T):
  v = do_case(f)
  print "Case #%d: %d" % (i+1, v))