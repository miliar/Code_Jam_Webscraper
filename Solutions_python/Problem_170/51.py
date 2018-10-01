import sys, string
from copy import copy, deepcopy
import gmpy
import time
import random

import sys
sys.setrecursionlimit(1000000)

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readbinlist():
	return [int(x,2) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()

def cost(phrase, en0, fr0):
    common = len(en0 & fr0)
    en1 = copy(en0)
    fr1 = copy(fr0)
    en2 = copy(en0)
    fr2 = copy(fr0)
    en1 |= phrase
    fr2 |= phrase
    return min(len(en1 & fr1), len(en2 & fr2)) - common

def is_eng(phrase, en0, fr0):
    #~ common = len(en0 & fr0)
    en1 = copy(en0)
    fr1 = copy(fr0)
    en2 = copy(en0)
    fr2 = copy(fr0)
    en1 |= phrase
    fr2 |= phrase
    return len(en1 & fr1) < len(en2 & fr2)

for t in range(T):
    N = readint()
    
    P = []
    for i in range(N):
        p = sys.stdin.readline().strip()
        P.append(set(p.split()))

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    
    en0 = P[0]
    fr0 = P[1]
    
    if N == 2:
        print len(en0 & fr0)
        continue
    
    Q = P[2:]
    
    best = 1e10
    for q in range(1000):
        en = copy(en0)
        fr = copy(fr0)
        
        random.shuffle(Q)
        
        for i in range(N-2):
            if is_eng(Q[i], en, fr):
                en |= Q[i]
            else:
                fr |= Q[i]
        
        best = min(best, len(en & fr))
    
    print best
