# -*- coding: utf-8 -*-

import sys

def flip(c):
    if c == '-':
        return '+'
    return '-'


def solve(S, K):
    nb_pancakes = len(S)
    i = 0
    nb_flips = 0
    while i < nb_pancakes:
        c = S[i]
        if c == '-':
            if i+K > nb_pancakes:
                return 'IMPOSSIBLE'
            for j in xrange(i,i+K):
                S[j] = flip(S[j])
            nb_flips += 1
        i += 1
    return str(nb_flips)


filename = sys.argv[1]
with open(filename) as f:
    n_cases = int(f.readline())
    for i in xrange(n_cases):
        S,K = f.readline().strip().split()
        S = list(S)
        K = int(K)
        res = solve(S,K)
        print 'Case #{}: {}'.format(i+1,res)
        
