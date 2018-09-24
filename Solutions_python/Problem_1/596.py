#!/usr/bin/python

import sys

inf = 1000000000

readline = sys.stdin.readline

n = int(readline())

for i in xrange(1, n + 1):
   last = ""
   bin = {last:inf}
   s = int(readline())
   for j in xrange(s):
      bin[readline()] = 0
   q = int(readline())
#print q
   oldmin = 0
   for j in xrange(q):
      new = readline()
#print new
      bin[last] = oldmin + 1
      newmin = bin[new] = bin[""] = inf
      for val in bin.values():
         if val < newmin:
            newmin = val
      oldmin = newmin
      last = new
#print bin
   print "Case #%d: %d" % (i, oldmin)

