#!/usr/bin/python
# -*- coding: utf-8 -*-
## Problem A. RPI (GCJ Round 1B 2011)


def rpis(N, tab):
	wp = [0]*N ## per team
	owp = [[] for k in xrange(N)] ## per team (not average)
	oowp = [[] for k in xrange(N)] ## per team (not average)
	
	for i, k in enumerate(tab):
		for h in xrange(N):
			kk = k[0:h] + k[h+1:]
			res = k[h]
			not_play = kk.count(".")
			win = kk.count("1")
			a = win / ((N-not_play-1)*1.0) ## wp for the team i \ h
			if h == i:
				wp[i] = a ## WP ok
			elif res != ".":
				owp[h].append(a) ## OWP ok
				#print i, h, kk, res, win, N-not_play-1, a, oowp
	
	owp_ok = [sum(k)/(1.0*len(k)) for k in owp] ## average
	#print owp_ok
	
	for i, k in enumerate(tab):
		for h in xrange(N):
			if h != i and k[h] != ".":
				a = owp_ok[i]
				oowp[h].append(a)
				#print i, h, a, oowp
	
	oowp_ok = [sum(k)/(1.0*len(k)) for k in oowp] ## average ok
	#print oowp_ok
	
	rpi = [] ## RPI
	for k in xrange(N):
		rpi.append(0.25*wp[k] + 0.50*owp_ok[k] + 0.25*oowp_ok[k])
	
	return rpi


if __name__ == "__main__":
	T = int(raw_input())
	for i in xrange(T):
		N = int(raw_input()) ## nb of teams
		tab = [raw_input().split()[0] for j in xrange(N)]
		
		sol = rpis(N, tab)
		char = "Case #%d:" %(i+1)
		print char
		for k in sol:
			print k