#!/usr/bin/env python

MAX = 10**100
r = [1,4,9]

def out(x):
	global r
	if x > MAX: return True
	if str(x)==str(x)[::-1]: r += [x]
	return False

def gen(a):
	b = a[::-1]
	if out(int(a+b)**2): return False
	for i in ('0','1','2'):
		out(int(a+i+b)**2)
	return True

x = 1
while gen(bin(x)[2:]): x += 1

x = '2'
while gen(x): x += '0'

r.sort()
for i in r: print i
