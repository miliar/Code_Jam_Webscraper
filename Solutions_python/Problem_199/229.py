__author__ = 'sware'

import sys

handle = file(sys.argv[1])
handleout = file(sys.argv[2], 'w')

for case in xrange(int(handle.readline())):
    S, K = handle.readline().split()
    K = int(K)
    S = [p == '+' for p in S]
    flips = 0
    for i in xrange(len(S)-K+1):
        if not S[i]:
            flips += 1
            for j in xrange(K):
                S[i+j] = not S[i+j]
    if sum(S) != len(S):
        handleout.write('Case #{}: {}\n'.format(case+1, 'IMPOSSIBLE'))
    else:
        handleout.write('Case #{}: {}\n'.format(case+1, flips))