#!/usr/bin/python3

import sys
import math
EPS = sys.float_info.epsilon

def readi(): return int(sys.stdin.readline())
def readis(): return [int(x) for x in sys.stdin.readline().split()]

def simple(S,X):
    l,r = 0,len(S)-1
    used = 0
    while l < r:
        used += 1
        if S[l] > X - S[r]:
            r -= 1
        else:
            r -= 1
            l += 1
    if l == r:
        used += 1
    return used


def case1():
    N, X = readis()
    S = readis()
    S = sorted(S)

    used = 0;
    for i in range(len(S)-1,-1,-1):
        if S[i] > X-S[0]:
            used +=1
            S.pop()
    r = simple(S,X)
    return used + r
    m = 0
    for i in range(len(S)):
        if S[i] > X//2: m+= 1
    if r > (len(S) + 1) // 2 and r > m:
        print(X, r, (len(S) + 1) // 2)
        print([(x,X-x) for x in S])



def case():
    N, X = readis()
    S = readis()
    S = sorted(S)
    #print(N, X)
    #print(S)
    l,r = 0,len(S)-1
    used = 0
    while l < r:
        used += 1
        if S[l] > X - S[r]:
            r -= 1
        else:
            r -= 1
            l += 1
    if l == r:
        used += 1
    return used


T = readi()
for i in range(T):
    print("Case #%s: %s" % (i+1, case()))


    

