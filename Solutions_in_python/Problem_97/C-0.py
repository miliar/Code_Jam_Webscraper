#!/usr/bin/env python
import math

N = int(raw_input())
for t in range(1,N+1):
    test = raw_input().split()
    a = int(test[0])
    b = int(test[1])
    sa = test[0]
    sb = test[1]

    r = 0
    for x in range(a,b):
        s= str(x)
        n= len(s)
        for y in range(0,n):
            v = s[y:n]+s[0:y]
            if sa <=s and s < v and v <= sb:
                #if int(sa) <= int(s) and int(s) < int(v) and int(v) <= int(sb):
                #   print "nice",
                #print "found",sa,"<=",s,"<",v,"<=",sb
                r+=1
    print 'Case #'+str(t)+':',r 

