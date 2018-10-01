#!/usr/bin/env python
#import psyco
#psyco.full()
from fractions import Fraction
def gint():
	return int(raw_input())

def gints():
	return [int(x) for x in raw_input().split()]

def solve():
	N = gint()
	dat = []
	for i in range(N):
		dat.append(raw_input())
	WP = []
	val = []
	for i in range(N):
		win = 0
		game = 0
		for c in dat[i]:
			if c != '.':
				game += 1
				if c == '1':
					win += 1
		WP.append(Fraction(win, game))
		val.append([win, game])
	OWP = []
	for i in range(N):
		owp = Fraction(0)
		count = 0
		for j in range(N):
			if dat[i][j] == '.': continue
			win, game = val[j]
			if dat[j][i] != '.':
				game -= 1
				if dat[j][i] == '1':
					win -= 1
			owp += Fraction(win, game)
			count += 1
		OWP.append(Fraction(owp, count))
	for i in range(N):
		oowp = Fraction(0)
		count =0 
		for j in range(N):
			if dat[i][j] != '.':
				oowp += OWP[j]
				count += 1
		if count > 0:
			oowp /= count
		else:
			oowp = 0
		RPI = 0.25 * float(WP[i]) + 0.5 * float(OWP[i]) + 0.25*float(oowp)
		print RPI

for i in range(1, gint()+1):
	print 'Case #%d:' % (i)
	solve()
