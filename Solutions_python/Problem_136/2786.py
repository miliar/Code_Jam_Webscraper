#!/usr/bin/env python

import sys

def rl():
  return sys.stdin.readline().strip()

def solve_one():
  C, F, X = [float(x) for x in rl().split()]
  rate = 2
  have = 0
  time = 0
  while True:
    Xtime = X/rate
    Ctime = C/rate + X/(rate+F)
    if Xtime < Ctime:
      return time+Xtime
    else:
      time += C/rate
      rate += F
  
def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
