#!/usr/bin/python3

import sys

t = int(sys.stdin.readline())

for i in range(t):
	l = sys.stdin.readline().split()
	n = int(l[0])
	sup = int(l[1])
	thr = int(l[2])
	l = l[3:3+n]
	ret = 0
	for k in range(len(l)):
		g = int(l[k])
		if g%3 == 1:
			if g//3+1 >= thr: ret += 1
			continue
		base = (g+1)//3
		if base >= thr:
			ret += 1
			continue
		if base+1 < thr:
			continue
		if base < 1:
			continue
		if sup >= 1:
			sup -= 1
			ret += 1
	print("Case #"+str(i+1)+": "+str(ret))
