# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:55:49 2015

@author: nibutler
"""

f = open('A-large.in', 'r')

f.readline()
c = 1
for line in f:
    values = line.split(" ")
    x = 0
    s = 0
    e = 0
    for n in values[1][:-1]:
        if s >= x:
            #print(n)
            s = s + int(n)
            x = x + 1
        else:
            e = x - s + e
            s = int(n) + x
            x = x + 1
    print "Case #" + str(c) +": " + str(e)
    c = c+1

f.close()