import operator
import itertools
import functools
import math

def getAll(c, pd):
    i = c+1
    arr = []
    while i <= N:
        if ds[i] <= ds[c] + pd:
           arr.append(i)
        i += 1
    return arr

def solve(c, pd):
    if (c, pd) in cache:
        return cache[(c, pd)]
    if ds[c] + pd >= D:
        cache[(c, pd)] = True
        return True
    pos = getAll(c, pd)
    for i in pos:
        if ds[i] - ds[c] > ls[i]:
            d = ls[i]
        else:
            d = ds[i] - ds[c]
        if solve(i, d):
            cache[(c, pd)] = True
            return True
    cache[(c, pd)] = False
    return False
     
fn = open('1.in')
ofn = open('1.out', 'w')
TC = int(fn.readline())
for tc in range(TC):
    N = int(fn.readline())
    ds = [0]
    ls = [0]
    for _ in xrange(N):
        d, l = map(int, fn.readline().strip().split())
        ds.append(d)
        ls.append(l)
    D = int(fn.readline())
        
    cache = {}
    #if ds[1] + ds[1] >= D:
    #    res = 'YES'
    #else:
        
    #current
    c = 1
    #previous
    p = 0
    res = 'NO'
    if solve(1, ds[1]):
        res = 'YES'
    
    print res            
    
    
    #print tc       
    print >>ofn, 'Case #{}: {}'.format(tc +1, res)
        
        
