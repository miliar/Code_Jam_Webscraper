#
#python 2.6

import math
import fractions

import time

INPUT_FILE = 'A-large.in'
OUT_FILE = 'A-small.out'
rf = file(INPUT_FILE)
wf = file(OUT_FILE, 'w')

caseNum = 0
def inputs():
    global caseNum
    if caseNum == 0:
        caseNum = rf.readline().strip()
        caseNum = int(caseNum)
    for i in xrange(caseNum):        
        N = int(rf.readline().strip())
        wirearray = []
        for k in xrange(N):
            strarray = rf.readline().strip().split()
            wirearray.append( [int(num) for num in strarray] )
        yield N, wirearray


def computey(N, wirearray):
    if N == 1:
        return 0
    elif N == 2:
        if wirearray[0][0] < wirearray[1][0] and wirearray[0][1] < wirearray[1][1]:
            return 0
        elif wirearray[0][0] > wirearray[1][0] and wirearray[0][1] > wirearray[1][1]:
            return 0
        return 1
        
    y  = 0
    for i in xrange(N):
        for j in xrange(i):
            y += computey(2, [wirearray[i],  wirearray[j]])
    return y
    
caseIndex = 1
for N, wirearray in inputs():
    y = computey(N, wirearray)
    wf.write('Case #{0}: {1}\n' .format(caseIndex,y)) 
    print 'Case #{0}: {1}' .format(caseIndex,y)
    caseIndex += 1

#print 'Done'
wf.close()
rf.close()
