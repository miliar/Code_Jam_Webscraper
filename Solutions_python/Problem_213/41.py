import sys
import numpy as np

def getWords():
    return sys.stdin.readline().strip().split()

def getInts():
    return np.array([int(i) for i in getWords()], dtype=np.int64)

def getInt():
	i = getInts()
	assert len(i)==1
	return i[0]

#sys.stdin = open('B.in')

T = getInt()
for caseNo in xrange(1,T+1):
    N, C, M = getInts()
    PB = np.asarray([getInts()-1 for m in xrange(M)]).T
    custMax = max(np.bincount(PB[1]))
    totalP = np.bincount(PB[0],minlength=N)
    cumP = np.cumsum(totalP)
    matchMin = (cumP + np.arange(N))//np.arange(1,N+1)
    rides = max(custMax, matchMin.max() )
    promos = (np.maximum(0, totalP - rides)).sum()
    
    print "Case #%d: %d %d"%(caseNo, rides, promos)
