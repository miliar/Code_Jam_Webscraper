#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,re

input = 'A-large.in'
output = 'A-large.out.txt'
f = file(input)
g = file(output,'w')

n_cases = int(f.readline().strip())

for k in range(n_cases):
    
    message = [ x for x in str(f.readline().strip()) ]
    num = []
    for ch in message:
        if not ch in num:
            num.append(ch)
#    print zip(num,range(len(num)))
    d = dict(zip(num,range(len(num))))
    d[num[0]]=1
    if len(d) > 1:
        d[num[1]]=0
#    print d
    
    sum = 0
    n = len(d)
    if len(d) == 1:
        n = 2
    message.reverse()
    for i in range(len(message)):
        sum += d[message[i]] * (n ** i)
    
    line = "Case #%d: %d" % (k+1, sum)
    
    print line
    g.write("%s\n" % line)

f.close()
g.close()
