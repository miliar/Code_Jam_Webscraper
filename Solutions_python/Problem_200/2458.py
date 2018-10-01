# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 01:12:28 2017

@author: wddwxy
"""

t = int(raw_input())  # read a line with a single integer
for ti in xrange(t):
    line = raw_input()
    num = list(line)
    for i in xrange(len(num)):
        num[i] = int(num[i])
    for i in xrange(len(num) - 1, 0, -1):
        if num[i] < num[i - 1]:
            num[i] = 9
            num[i - 1] -= 1
    if num[0] == 0:
        num = num[1:]
    for i in xrange(1, len(num)):
        if num[i] < num[i - 1]:
            num[i] = num[i - 1]
    print "Case #" + str(ti + 1) + ": " + ''.join(str(x) for x in num)