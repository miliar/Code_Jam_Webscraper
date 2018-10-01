#!/usr/bin/python

import sys

fp = open(sys.argv[1],"r")
T = int(fp.readline())
a = 101*[0]
for n in range(1,101):
  for d in range(1,n+1):
    for w in range(1,d+1):
      if 100*w % d == 0 and a[100*w/d] == 0:
        a[100*w/d] = d
# at least a[p] times one has to play for percentage p to be an integer

for i in range(T): # for all cases
  v1 =  map(int,(fp.readline().split()))
#  print v1
  n = v1[0]
  pd = v1[1]
  pg = v1[2]
  if (pg==0 and pd==0) or (pd == 100 and pg == 100) or (pd > 0 and pg > 0 and pg < 100 and a[pd]<=n):
    r = "Possible"
#    if pd > 0:
#      print str(100/pd)
  else:
    r = "Broken"
  print "Case #"+str(i+1)+": "+r

