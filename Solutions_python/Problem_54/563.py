#!/usr/bin/python3
# -*- coding: utf-8 -*-

def gcd(a,b):
	while(b):
		(a,b) = (b, a%b)
	return a

ntests = int(input())

for tt in range(1, ntests+1):
	L = [int(x) for x in input().split()][1:]
	L.sort()
	g = 0
	for i in range(len(L)-1):
		if(L[i]!=L[i+1]):
			g = gcd(L[i+1]-L[i], g)
	assert(g!=0)
	print("Case #", tt, ": ", (g - L[0]%g)%g, sep='')
