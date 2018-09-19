#
#python 2.6

import math
import fractions

import time

INPUT_FILE = 'A-large.in'
OUT_FILE = 'A-large.out'
rf = file(INPUT_FILE)
wf = file(OUT_FILE, 'w')

caseNum = 0
def inputs():
    global caseNum
    if caseNum == 0:
        caseNum = rf.readline().strip()
        caseNum = int(caseNum)
    for i in xrange(caseNum):        
        strarray = rf.readline().strip().split()
        N, M = [int(num) for num in strarray]
        narray = []
        for j in xrange(N):
            narray.append(rf.readline().strip('/').strip())
        marray = []
        for k in xrange(M):
            marray.append(rf.readline().strip('/').strip())
        yield N, M, narray, marray


def computey(N, M, narray, marray):
    caches = set()
    for i in xrange(N):
        caches.add(narray[i])
        currend = -1
        currindex = narray[i].rfind('/', 0, currend)
        while currindex != -1:            
            currend = currindex
            caches.add(narray[i][:currindex])
            currindex = narray[i].rfind('/', 0, currend)
            
    sum = 0
    for j in xrange(M):
        if marray[j] in caches:
            continue 
        sum += 1
        caches.add(marray[j])
        currend = -1
        currindex = marray[j].rfind('/', 0, currend)
        while currindex != -1:
            currend = currindex
            if marray[j][:currindex] in caches:
                break
            caches.add(marray[j][:currindex])
            sum += 1     
            currindex = marray[j].rfind('/', 0, currend)
    return sum
    
caseIndex = 1
for N, M, narray, marray in inputs():
    y = computey(N, M, narray, marray)
    wf.write('Case #{0}: {1}\n' .format(caseIndex,y)) 
    print caseIndex, ':',  y
    caseIndex += 1

print 'Done'
wf.close()
rf.close()
