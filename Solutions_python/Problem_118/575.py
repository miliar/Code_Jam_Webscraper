#!/usr/bin/python3

import math

def check(a):
	b = list(str(a))
	c = list(str(a))
	b.reverse()
	#print(c, ' ', b)
	return (b == c)

def get(max_val):
	palins = []
	for i in range(1, max_val):
		if (check(i) == True and check(i * i) == True):
			palins.append(i * i)
	return palins

ans = get(10000000)
t = int(input())
for i in range(1, t + 1):
	a, b = (input().split(' '))
	a = int(a)
	b = int(b)
	res = 0
	for j in ans:
		if (a <= j <= b):
			res += 1
	print('Case #{0}: {1}'.format(i, res))
