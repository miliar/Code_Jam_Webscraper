#!/usr/bin/python2
from sys import stdin

C = int(stdin.readline())
for c in range(1,C+1):
  n = 0
  t = map(int, stdin.readline()[:-1].split())
  l = t[3:]
  l.sort()
  l = l[::-1]
  #print l
  #print t
  for i in l:
    if (i + 2) / 3 >= t[2]:
      n += 1
      #print ",",
    elif ((i + 1) / 3) + 1 >= t[2] and t[1] > 0 and i > 1:
      n += 1
      t[1] -= 1
      #print ".",
    else:
      break
  #print "'" + t + "'"
  print "Case #%d: %s" %(c, n)
