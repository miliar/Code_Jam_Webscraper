'''
Created on 2010-5-8

@author: fanzy
'''
import sys

def pre(groups, k):
    l = len(groups)
    
    temp = sum(groups)
    if temp <= k:
        data = [(temp, i) for i in range(l)]
        return data
    
    data = [0] * l
    for i in range(l):
        j = i
        s = 0
        g = groups[j]
        while s + g <= k:
            s += g
            j = (j + 1) % l
            g = groups[j]
        data[i] = (s, j)
    return data

def ride(data, r):
    offset = 0
    S = 0
    for i in xrange(r):
        s,j = data[offset]
        S += s
        offset = j
    return S

f = open(sys.argv[1])
C = int(f.readline().strip())
for tc in range(C):
    r, k, n = [int(s) for s in f.readline().strip().split()]
    groups = [int(s) for s in f.readline().strip().split()]
    print "Case #%d: %d" % (tc+1, ride(pre(groups, k), r))






