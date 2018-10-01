#!/usr/bin/env python

from operator import mul

def improve(P,U):
  #print "Improve: ", U, P
  if (U>0):
    P.sort()
    smallest = P[0]
    if (smallest < 1.0):
      nr_smallest = P.count(smallest)
      if nr_smallest < len(P):
        smallest2 = P[nr_smallest]
      else:
        smallest2 = float("inf")
      if (smallest+(U/nr_smallest)) > smallest2:
        # Special case
        used = 0
        for i in xrange(nr_smallest):
          used += (smallest2-P[i])
          P[i]=smallest2
        P = improve(P,U-used)
      else:
        for i in xrange(nr_smallest):
          P[i]+=U/nr_smallest
    
  return P

def solve(case_nr):
  [N,K] = map(int, raw_input().split())
  
  U = float(raw_input())
  P = map(float, raw_input().split())
  
  #print N,K,U,P
  P = improve(P,U)

  print "Case #%d: %.6f" % (case_nr, reduce(mul,P,1))


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
