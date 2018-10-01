#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import ceil, log
        
def main():
    fName = 'B-large'
    fIn = open("%s.in" % fName, 'r')
    fOut = open("%s.out" % fName, 'w')
    
    for t in xrange(int(fIn.readline().strip())):
    
        l, p, c = map(int, fIn.readline().strip().split())
        
        x = 0
        q = l
        while q*c < p:
            q *= c
            x += 1
        y = 0
        q = p
        while ceil(float(q) / c) > l:
            q = ceil(float(q) / c)
            y += 1   
        
        s = min((x,y))
    
        r = 0
        while s > 0:
            r += 1
            s = ceil((s - 1.0) / 2)
    
        #print "Case #%s: %s\n" % (t+1, r)
        fOut.write("Case #%s: %s\n" % (t+1, r))
        
if __name__ == '__main__': main()
