#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(1010)

def war1(naomi, ken):
	if naomi == []:
		return 0
	if naomi[0] < ken[0]:
		naomi.pop(-1)
		ken.pop(0)
		return 0 + war1(naomi, ken)
	k = 1
	while k < len(naomi) and naomi[k] > ken[0]:
		k += 1
	naomi.pop(k-1)
	ken.pop(0)
	return 1 + war1(naomi, ken)

def war2(naomi, ken):
	if naomi == []:
		return 0
	if naomi[0] < ken[0]:
		naomi.pop(0)
		ken.pop(0)
		return 0 + war2(naomi, ken)
	if naomi[0] > ken[0]:
		naomi.pop(0)
		ken.pop(-1)
		return 1 + war2(naomi, ken)

def war(t):
	N = int(t[0])
	naomi1 = sorted(map(float, t[1].split(" ")), reverse=True)
	ken1 = sorted(map(float, t[2].split(" ")), reverse=True)
	naomi2 = []
	naomi2.extend(naomi1)
	ken2 = []
	ken2.extend(ken1)
	return "%s %s"%(war1(naomi1, ken1), war2(naomi2, ken2))



if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		buf = f.read()
	t = buf.split("\n")
	nb_boards = int(t[0])
	t = t[1:]
	for k in xrange(0, nb_boards):
		print "Case #%d: %s"%(k+1, war(t[k*3:k*3+3]))
