#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
testCaseTotal = int(raw_input())  # read a line with a single integer
for testCase in xrange(1, testCaseTotal + 1):
    D, N = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    horses = []
    for i in xrange(0, N):
        ki, si = [int(s) for s in raw_input().split(" ")]
        horses.append([ki, si])
    shs = sorted(horses, key=lambda h:h[1])
    
    #print shs
    
    ph = shs[0]
    fhs = [ph]
    for h in shs[1:]:
        if h[0] < ph[0]:
            ph = h
            fhs.append(ph)
    
    #print fhs
    
    ph = fhs[0]
    tm = (D - ph[0]) * 1.0 / ph[1]
    result = D / tm
    for h in fhs[1:]:
        if h[1] >= result:
            break
        tmdd = (D - h[0]) * 1.0 / h[1]
        if tmdd > tm:
            tm = tmdd
            result = D / tm 
    
    print "Case #%d: %.6f"% (testCase, result)
