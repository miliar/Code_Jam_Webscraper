import sys
import math
'''
f = open("/Users/burganovb/OneDrive/CodeJam17/A-small-practice.in")
lines = f.readlines()
f. close
t = int(lines[0])
'''
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    #N, K = [int(s) for s in lines[i].split(' ')]
    N, K = [int(s) for s in raw_input().split(' ')]

    m=int(math.log(K,2))
    n=K-2**m
    empty = N-2**m+1 #empty after 2**m-1 splits
    l = empty - int((empty)/2**m)*2**m
    lastint = empty/2**m-1
    if n<l:
        lastint += 1

    print "Case #{}: {} {}".format(i, lastint-lastint/2, lastint/2)

