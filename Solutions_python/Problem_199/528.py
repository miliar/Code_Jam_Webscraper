import sys
from fractions import gcd
import numpy as np

lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

for line in lines[1:]:
    casenum += 1
    vals = line.split()
    S = '+' + vals[0] + '+'
    K = int(vals[1])

    T = [0]*(len(S)-1)
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            T[i] = 1


    flips = 0

    for i in xrange(len(T)-K):
        if T[i] == 1:
            flips += 1
            T[i+K] = T[i+K] ^ 1
                
    for i in xrange(len(T)-K, len(T)):
        if T[i] == 1:
            print 'case #' + str(casenum) + ": IMPOSSIBLE"
            break
        if i == len(T)-1:
            print 'case #' + str(casenum) + ": " + str(flips)



        
