#! /usr/bin/env python

def lastAppear(pos, se, w):
    last = -1;    
    for i in se:
        try:
            r = w.index(i, pos)
        except ValueError:
            return len(w)
        if r > last:
            last = r
    pos = last
    return pos
             


n = input()
for i in range(0, n):
    pos = 0
    nChange = 0
    s = input()
    se = []
    for j in range(0, s):
        se.append(raw_input())
    nw = input()
    w = []
    for h in  range(0, nw):
        w.append(raw_input())    
    while pos < len(w):
        pos = lastAppear(pos, se, w)
        nChange += 1
    if nChange == 0:
        nChange = 1
    print "Case #"+str(i+1)+": "+ str(nChange-1)
        


