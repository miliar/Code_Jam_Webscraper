#!/usr/bin/env python
from sys import stdin, stdout
from itertools import *
import multiprocessing

def answer(data):
	X,S,R,T,N,ww = data

	ww = sorted(ww)
	unas = 0
	last = 0
	for b,e,w in ww:
		unas += b-last
		last = e
	unas += X - last

	T = float(T)
	ct = 0.0
	ww = [(0, float(unas))] + sorted([(w, float(e-b)) for b,e,w in ww])
	for sp,l in ww:
		t = min(T, l/(R+sp))
		T -= t
		ct += t
		l -= t * (R+sp)
		ct += l/(S+sp)

	return ct

def cases(s):
	while 1:
		X,S,R,T,N = map(int, s.next().split())
		dat = [ map(int, l.split()) for l in islice(s, N) ]
		yield (X,S,R,T,N,dat)

if __name__ == '__main__':
	stdin.next()
	p = multiprocessing.Pool(6)
	for n,ans in enumerate(p.map(answer, cases(stdin))):
		print "Case #%d: %s" % (n+1, ans)
