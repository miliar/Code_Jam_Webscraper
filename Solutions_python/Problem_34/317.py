#! /usr/bin/env python
#coding=utf-8
#Author: Xiongfei GUO @ SSPU

import re

f = open('datain.txt', 'r')
fo = open('dataout.txt', 'w')

L,D,N = map(int, f.readline().split(' '))
#print L, D, N

testin = []
pattern = []
for i in range(D):
    testin.append(f.readline().replace('\n', ''))
    
for i in range(N):    
    pattern.append(f.readline().replace('\n', '').replace('(', '[').replace(')', ']'))
    
#print testin
#print pattern

p = 1
for pat in pattern:
    pat = re.compile(pat)
    fo.write( 'Case #%d: %d\n' % (p, len(filter(lambda x:(re.findall(pat, x) != []), testin))) )
    p += 1

f.close()
fo.close()