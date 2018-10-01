#!/usr/bin/env python

import heapq
import math

cases = raw_input()
for c in range(int(cases)):
    n,k=raw_input().strip().split()
    n=int(n); k=int(k)


    # heuristic to save a lot of time!!
    # number of nodes in last row is 
    # all insertions after
    # 2^int(log(n,2)))
    
    if k>2**(math.log(n,2)):
      print "Case #%i: 0 0" % ( (c+1))

    else:
      stalls = [-1*n]
      heapq.heapify(stalls)
      #print "===="
      #print stalls
      while k>0:
        longest = heapq.heappop(stalls)
        l=r=0
        if longest%2==0:
          l=(longest/2)+1
          r=(longest/2)
        else:
          l=r=(longest+1)/2
           
        if k==1:
          l=-1*l; r=-1*r 
          y = max(l,r)
          z = min(l,r)
          print "Case #%i: %i %i" % ( (c+1), y, z)
  
        if l != 0:
          heapq.heappush(stalls,l)
        if r != 0:
          heapq.heappush(stalls,r)
  
        #print stalls
        k-=1
