from __future__ import print_function
import sys
import numpy as np
import math

def getminmax(x, r):
    low = ((x * 10)+(11*r)-1) // (11*r)
    high = (x * 10) // (9*r)
    if low <= high:
        return (low, high)
    return (0,0)

def overlaps(x, y):
    return x[0] <= y[1] and y[0] <= x[1]

def getnumpackages(N, P, R, plist):
    #Get min, max servings
    mmlist = []
    for x in range(N):
        mmlist.append([])
        line = np.sort(plist[x])
        for y in range(P):
            z = getminmax(line[y], R[x])
            if z[1] != 0:
                mmlist[x].append(z)
    #Go through list finding packages
    count = 0
    ilist = [0] * N
    for x in mmlist[0]:
        found = True
        for row in range(1,N):
            if ilist[row] >= len(mmlist[row]):
                return count
            while mmlist[row][ilist[row]][1] < x[0]:
                ilist[row] += 1
                if ilist[row] >= len(mmlist[row]):
                    return count
            if not overlaps(x, mmlist[row][ilist[row]]):
                found = False
                break
        if found:
            count += 1
            for row in range(1,N):
                ilist[row] += 1
                
    return count

#Read data
if len(sys.argv) < 2:
    print("Missing input file name")
    quit()
with open(sys.argv[1], "r") as f:
    T = int(f.readline())
    for x in range(T):
        plist = []
        N, P = [int(z) for z in f.readline().split()]
        R = [int(z) for z in f.readline().split()]
        for y in range(N):
            plist.append([int(z) for z in f.readline().split()])
        print("Case #%d: %d" % (x + 1, getnumpackages(N, P, R, plist)))
