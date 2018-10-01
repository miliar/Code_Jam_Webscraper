from __future__ import print_function
s = """3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10"""
# s = open('A-small-attempt1.in').read()
s = open('A-large.in').read()
"""
Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333"""
import sys
import math

ss = s.split('\n')
T = int(ss[0])

f = open('A.out', 'w')
# f = sys.stdout

idx = 1
for j in range(0, T):
    dn = ss[idx].split(' ')
    D = int(dn[0])
    N = int(dn[1])
    idx += 1
    K = []
    S = []
    maxKS = []
    max_ks = 1e15
    for n in range(0, N):
        ks = ss[idx].split(' ')
        idx += 1
        k = int(ks[0])
        s = int(ks[1])
        m = (D*s)/float(D-k)
        K.append(k)
        S.append(s)
        maxKS.append(m)
        if m < max_ks:
            max_ks = m
            # print(D,s,k)
    # print(min(maxKS), max_ks)
    print('Case #%d: %.6f'%(j+1,max_ks), file=f)