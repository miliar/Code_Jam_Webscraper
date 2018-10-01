# -*- coding: utf-8 -*-

"""
For small case
"""

from __future__ import print_function, division
import sys
if sys.version > '3':
    from past.builtins import xrange, raw_input
    
import math
    
f = open('C-small.in', 'r')
out = open('answer.txt', 'w+')

t = int(f.readline())
for i in xrange(t):
    n, q = (int(ch) for ch in f.readline().split())
    e, s = [], []
    for j in xrange(n):
        tmp_e, tmp_s = (int(ch) for ch in f.readline().split())
        e.append(tmp_e)
        s.append(tmp_s)
    time = [math.inf for j in xrange(n)]
    cur_e, cur_s = e[0], s[0]
    distance = [0]
    time[0] = 0
    for j in xrange(n):
        matrix = [int(ch) for ch in f.readline().split()]
        if j < n - 1:
            distance.append(matrix[j + 1])
    for j in xrange(1, n):
        distance[j] += distance[j - 1]
    for j in xrange(1, n):
        for k in xrange(0, j):
            if e[k] >= distance[j] - distance[k]:
                time[j] = min(time[j], time[k] + (distance[j] - distance[k]) / s[k])
    #print(time,distance, e, s)        
    for j in xrange(q):
        tmp_u, tmp_v = (int(ch) for ch in f.readline().split())
    out.write('Case #' + str(i + 1) + ': ' + "{:.8f}".format(time[n - 1]) +'\n')

f.close()
out.close()