#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import random

def token(f):
	ws = ' \t\n'
	while True:
		c = f.read(1)
		if c not in ws: break
	l = [c]
	while True:
		c = f.read(1)
		if c in ws: break
		l.append(c)
	return ''.join(l)

def rt(): return token(sys.stdin)
def ri(): return int(rt())
def rf(): return float(rt())
EPS = 10**-9

def sqdist(a, b):
	dx = a[0]-b[0]
	dy = a[1]-b[1]
	return dx*dx + dy*dy

def rp():
	return (random()*w, random()*l)

def isok(pn, rn):
	for (p,r) in pts:
		if sqdist(p,pn) + EPS < (r+rn)**2:
			return False
	return True

def gennext():
	global pts
	rnow = rs[len(pts)]
	trial = 0
	while trial<1000:
		trial += 1
		pt = rp()
		if isok(pt, rnow):
			pts.append((pt, rnow))
			print>>sys.stderr, len(pts)
			return
	pts = []

tests = ri()
for case in xrange(1,tests+1):
	n, w, l = ri(), ri(), ri()
	pts = []
	rs = [ri() for _ in xrange(n)]
	while len(pts) < n:
		gennext()
			
	print "Case #%d:"%case,
	for (pt,_) in pts:
		print pt[0],pt[1],
	print
			
