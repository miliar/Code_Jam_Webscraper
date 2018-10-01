from __future__ import division
import sys, re
readline = sys.stdin.readline

N = int(readline())
for case in range(1, 1 + N):
    numflies = int(readline())
    vecall=[0,0,0,0,0,0]
    for i in xrange(0,numflies):
        inc=[int(word) for word in readline().split()]
        vecall=[a+b for (a,b) in zip(vecall,inc)]
    vecall=[a/numflies for a in vecall]
    (x,y,z,vx,vy,vz)=vecall
    try:
        t=-(x*vx+y*vy+z*vz)/(vx**2+vy**2+vz**2)
    except ZeroDivisionError:
        t = 0
    t=max(0,t)
    xt=x+vx*t
    yt=y+vy*t
    zt=z+vz*t
    dt = (xt**2+yt**2+zt**2)**0.5
    print "Case #%s: %f %f"%(case,dt,t)
    
    
    
        
    
