# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:27:32 2013

@author: Melissa
"""
import math

f = open("C-large-1.in")
answer = open("C-answer-large.txt", 'w')

T = int(f.readline())

def pal(n):
    s = str(n)
    s_rev = s[::-1]
    return s == s_rev
        
limits = []
for line in f:
    l = map(int, line.split(" "))
    limits.append(l)

mi = min((l[0]) for l in limits)
mx = max((l[1]) for l in limits)

palindromes = []
for i in xrange(int(math.sqrt(mi)), int(math.sqrt(mx))+1):
    if pal(i):
        s = i**2
        if pal(s):
            palindromes.append(s)

for i,l in enumerate(limits):
    result = 0
    for p in palindromes:
        if p >= l[0] and p <= l[1]:
            result += 1
        if p > l[1]:
            break
    answer.write("Case #%d: %d\n" % (i+1, result))

f.close()
answer.close()