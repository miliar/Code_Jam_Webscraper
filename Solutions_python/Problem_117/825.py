from __future__ import division
import sys, string
import itertools
from math import *

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

def transpose(M):
    return map(list, zip(*M))

def try_mow(S, M, i):
    line = M[i]
    H = max(line)
    
    # let's mow
    for j,h in enumerate(S[i]):
        if h > H:
            S[i][j] = H

for k in range(T):
    print >> sys.stderr, k
    m,n = readlist()
    M = []
    S = []
    for i in range(m):
        M.append(readlist())
        S.append([100] * n)
    
    for i in range(m):
        try_mow(S, M, i)
    
    M = transpose(M)
    S = transpose(S)

    for i in range(n):
        try_mow(S, M, i)

    M = transpose(M)
    S = transpose(S)

    for i in range(m):
        try_mow(S, M, i)
        
    print >> sys.stderr, "\n".join([str(x) for x in S])
    #print "\n".join([str(x) for x in S])
    
    ans = "YES" if S == M else "NO"
    print "Case #%d: %s" % ((k+1), ans)
