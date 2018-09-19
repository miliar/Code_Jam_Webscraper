# https://code.google.com/codejam/contest/2994486/dashboard#s=p1

import sys

def readline():
    return sys.stdin.readline().rstrip()

def count_pairs(a, b, k):
    pairs = 0
    for i in range(a):
        for j in range(b):
            n = i & j
            if n < k:
                pairs+=1
    return pairs

t = int(readline())
for case in range(t):
    line = readline()
    (a, b, k) = [int(s) for s in line.split()]
    pairs = count_pairs(a, b, k)
    print 'Case #{}: {}'.format(case+1, pairs)



