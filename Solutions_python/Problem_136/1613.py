#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in xrange(t):
  cfx = [float(x) for x in f.readline().split()]
  total_time = float(0)
  rate = float(2)
  buy = cfx[0]/rate + cfx[2]/(rate+cfx[1])
  wait = cfx[2]/rate
  while (buy < wait):
    total_time += (cfx[0]/rate)
    rate += cfx[1]
    buy = cfx[0]/rate + cfx[2]/(rate+cfx[1])
    wait = cfx[2]/rate
  total_time += cfx[2]/rate

  print "Case #" + str(case+1) + ":", str(total_time)
