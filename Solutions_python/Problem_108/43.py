#from __future__ import division
import sys, string
import itertools
from math import *

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())
global LB, LT, N, M

for k in range(T):
    
    N = int(sys.stdin.readline());
    D = []
    L = []
    for i in range(N):
        DL = readlist();
        D.append(DL[0]);
        L.append(DL[1]);
    Dtotal = int(sys.stdin.readline());
    print >> sys.stderr, D, L, Dtotal

    s0 = (0, D[0])
    Q = [s0]
    i = 0;
    ans = "NO"
    while i < len(Q):
        #~ print >> sys.stderr, i,Q
        s = Q[i]
        pos, leng = s  
        # aici sunt acum
        # pot sa ajung pana la pos+len*2
        if pos + leng*2 >= Dtotal:
            ans = "YES"
            break
        # sau pot sa prind lianele aflate intre pos+leng si pos+leng*2
        for j in range(N):
            if D[j] > pos+leng and D[j] <= pos+leng*2:
                newpos = D[j] - min(L[j], D[j] - pos-leng)
                newleng = D[j] - newpos
                #print newpos, D[j], newleng
                new = (newpos, newleng)
                #~ print >> sys.stderr, "s: %s, d:%d => %s" % (s, D[j], new)
                #~ if L[j] >= newleng:
                if new not in Q:
                    Q.append(new)
                #~ else: print "too short"
        i += 1
        
    
    print "Case #%d: %s" % ((k+1), ans)
    
    
