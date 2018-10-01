#! /usr/bin/python

import sys

T = int(sys.stdin.readline().rstrip("\n"))
for prob in xrange(1,T+1):
  pos = dict()
  pos["O"] = 1
  pos["B"] = 1
  ans = 0
  pre = 0
  prevcolor = "O"

  tests = sys.stdin.readline().rstrip("\n").split()
  nt = int(tests[0])
  tests = tests[1:]
  
  for i in xrange(nt):
    c = tests[2*i]      # color
    m = int(tests[2*i+1])   # pos
    if c == prevcolor:
      tp = abs(m-pos[c]) + 1
      pre += tp
      ans += tp
      pos[c] = m
    else:
      tp = abs(m-pos[c]) - pre
      if tp < 0: tp = 0
      tp += 1
      pre = tp
      prevcolor = c
      ans += tp
      pos[c] = m
  print "Case #%d: %d"%(prob,ans)
