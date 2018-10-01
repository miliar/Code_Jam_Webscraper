from __future__ import print_function
import sys

cases = int(sys.stdin.readline())

for n in range(1, cases+1):
    y, z = 0, 0
    numblocks = int(sys.stdin.readline())
    a = [float(i) for i in sys.stdin.readline().strip().split()]
    b = [float(i) for i in sys.stdin.readline().strip().split()]
    # y
    a.sort()
    b.sort()
    i, j = 0, 0
    while i<numblocks and j<numblocks:
        if a[i]<b[j]:
            i += 1
        else:
            y += 1
            i += 1
            j += 1
    # z
    i, j = 0, 0
    while i<numblocks and j<numblocks:
        if b[j]<a[i]:
            j += 1
        else:
            z += 1
            i += 1
            j += 1
    z = numblocks-z
    print('Case #'+repr(n)+': '+repr(y)+' '+repr(z))
