# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:48:05 2017

@author: wddwxy
"""

t = int(raw_input())  # read a line with a single integer
for ti in xrange(t):
    line = raw_input().split(' ')
    pancakes = line[0]
    k = int(line[1])
    l = [1] * len(pancakes)
    for i in xrange(len(pancakes)):
        if pancakes[i] == '-':
            l[i] = -1
    ans = 0
#    print l
    for i in xrange(0, len(pancakes) - k + 1):
#        print l
        if l[i] == -1:
            for j in xrange(i, i + k):
                l[j] *= -1
            ans += 1
        
    b = True
    for i in xrange(len(pancakes)):
        if l[i] == -1:
            b = False
            break
    if b:
        print "Case #" + str(ti + 1) + ": " + str(ans)
    else:
        print "Case #" + str(ti + 1) + ": " + "IMPOSSIBLE"
            