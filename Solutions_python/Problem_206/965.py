import sys
import math
from collections import deque
import sets
import itertools
import copy

def solve(t):
    D, N = map( int, sys.stdin.readline().strip().split() )
    ks = []
    ss = []
    for i in range(0, N):
         Ki, Si = map( int, sys.stdin.readline().strip().split() )
         ks.append(Ki)
         ss.append(Si)
    ts = []
    for i in range(0, N):
        ts.append( float(float(D-ks[i]) / float(ss[i])) )
    max_time = max( ts )
    res = float(D)/max_time
    str_res = "%0.6f" % res
    print "Case #"+str(t+1)+": "+str_res
    
         

T = int(sys.stdin.readline().strip())
for i in range(0, T):
    solve(i)
    #print "Case #"+str(i+1)+": "+"".join(map(str, n))
