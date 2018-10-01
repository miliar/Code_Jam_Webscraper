# Vladimir Burian, 2017 (vladaburian@gmail.com)

import string
import sys
import math
from itertools import *
import operator
from collections import Counter
import copy

class Tee:
    def __init__(self, ofile):
        self.file = ofile

    def write(self, ostr):
        sys.stdout.write(ostr)
        self.file.write(ostr)

    def close(self):
        self.file.close()

def read_int(fin):
    return int(fin.readline())

def read_ints(fin):
    return [int(x) for x in fin.readline().split()]

###############################################################################

def solve(fin):
    N,P = read_ints(fin)
    R = read_ints(fin)
    Q = [read_ints(fin) for _ in xrange(N)]
    
    for i in xrange(N):
        for j in xrange(P):
            lb = (10*Q[i][j] + 11*R[i] - 1) // (11*R[i])
            ub = (10*Q[i][j]) // (9*R[i])
            
            if ub < lb:
                Q[i][j] = None
            else:
                Q[i][j] = (lb, ub)
    
        Q[i] = [q for q in Q[i] if q is not None]
        Q[i] = sorted(Q[i])
    
    cnt = 0
    
    while True:
        if any(len(Q[i]) == 0 for i in xrange(N)):
            break
    
        maxmin = max(Q[i][0][0] for i in xrange(N))
        
        rep = False
        
        for i in xrange(N):
            if Q[i][0][1] < maxmin:
                Q[i] = Q[i][1:]
                rep = True

        if rep:
            continue
        
        maxmin = max(Q[i][0][0] for i in xrange(N))
        minmax = min(Q[i][0][1] for i in xrange(N))
        assert(maxmin <= minmax)
        
        cnt += 1
        
        for i in xrange(N):
            Q[i] = Q[i][1:]

    return cnt

###############################################################################

name = "test"
name = "B-small-attempt0"
name = "B-large"

sys.setrecursionlimit(5000)

fin = open(name+".in", "r")
fout = open(name+".out", "w")
fout = Tee(fout)

T = int(fin.readline())

for t in range(1,T+1):
    r = solve(fin);
    print >> fout, "Case #{}: {}".format(t, r)
    sys.stdout.flush()

fout.close()

print "=== DONE ==="

