import sys, string
import time
import random
import math

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def flip(S,i0,K):
    S = list(S)
    for i in range(i0,i0+K):
        S[i] = "-" if S[i] == "+" else "+"
    S = "".join(S)
    return S

def solve(S, K):
    #~ print S, K
    Q = [S]
    L = [0]
    i = 0
    while i < len(Q):
        s,l = Q[i],L[i]
        #~ print s
        if "-" not in s:
            return l
        for i0 in range(0, len(S)-K+1):
            m = flip(s, i0, K)
            #~ print s, i0, m
            if m not in Q:
                Q.append(m)
                L.append(l+1)
        i += 1
    return "IMPOSSIBLE"

T = readint()
for t in range(T):
    S, K = sys.stdin.readline().strip().split(" ")
    K = int(K)

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    print solve(S, K)
