#!/usr/bin/env python

def solve(S, K):
    def invert(S):
        L = ''
        for i in range(len(S)):
            L += (S[i] == '+') and '-' or '+'
        return L

    flips = 0
    
    while True:
        i = S.find('-')
        if i == -1:
            return flips
            
        if i > len(S) - K:
            return None
            
        S = S[:i] + invert(S[i:i + K]) + S[i + K:]
            
        flips += 1

T = int(input().strip())
for t in range(T):
    S, K = input().strip().split()
    K = int(K)
    
    flips = solve(S, K)
        
    if flips == None:
        solution = 'IMPOSSIBLE'
    else:
        solution = flips
        
    print('Case #%d: %s' % (t + 1, str(solution)))
