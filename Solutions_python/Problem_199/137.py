#!/usr/bin/env python3

def flip(S, K, i):
    for j in range(K):
        if S[i+j] == '-':    S[i+j] = '+'
        else:                S[i+j] = '-'

T = int(input())
for t in range(1,T+1):
    S, K = input().split()
    K = int(K)
    N = len(S)
    S = list(S)
    flips = 0
    for i in range(N):
        if flips >= 0:
            if S[i] == '-':
                if i > N - K:
                    flips = -1
                else:
                    flips += 1
                    flip(S, K, i)
    if flips >= 0:
        print('Case #%d: %d'%(t,flips))
    else:
        print('Case #%d: IMPOSSIBLE'%t)
       
