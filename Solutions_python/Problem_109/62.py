#!/usr/bin/env python
import sys
import math

def dist(a, b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

T = int(raw_input())
for t in xrange(T):
    N,W,L = map(int, raw_input().split())
    r = map(int, raw_input().split())
    pos = []
    for i in xrange(len(r)):
        found = False
        for a in xrange(W/r[i]+1):
            if found: break
            for b in xrange(L/r[i]+1):
                new_x = a * r[i]
                new_y = b * r[i]
                ok = True
                for j in xrange(len(pos)):
                    if dist( (new_x, new_y), pos[j] ) < r[j]+r[i]:
                        ok = False
                        break
                if ok:
                    found = True
                    pos.append( (new_x, new_y) )
                    break

    res = ["%f %f"%(i[0],i[1]) for i in pos]
    print "Case #%d: %s" % (t+1, " ".join(res))


