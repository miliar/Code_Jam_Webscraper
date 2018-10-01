from __future__ import print_function
import sys
import numpy as np
import math

def getans(N, K, plist):
    tot = 0
    plist = sorted(plist, key=lambda x:x[2], reverse=True)
    plist = np.array(plist)
    tot = plist[0:K-1,2].sum()
    flat = 0
    if K > 1:
        flat = max(plist[0:K-1,0])
        tot += flat**2
    findlast = plist[K-1:]
    findlast = findlast[:,2] + (findlast[:,0] ** 2 - flat ** 2) * (findlast[:,0] > flat)
    tot += max(findlast)
    return tot * math.pi

#Read data
if len(sys.argv) < 2:
    print("Missing input file name")
    quit()
with open(sys.argv[1], "r") as f:
    T = int(f.readline())
    for x in range(T):
        plist = []
        N, K = [int(z) for z in f.readline().split()]
        for y in range(N):
            R, H = [int(z) for z in f.readline().split()]
            plist.append([R, H, 2*R*H])
        print("Case #%d: %.9f" % (x + 1, getans(N, K, plist)))
