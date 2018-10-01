#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 05:44:25 2017

@author: ska
"""
def flipper(ar,k):
	a = ""
	i =0
	b = 0
#	n = 0
	c = ar[:]
	while i < (len(ar)-k+1):
		b = i
		if ar[i] == "-":
#			print(b)
			for j in range(i,i+k):
				if ar[j]=="+":
					a += "-"
				else:
					a += "+"
			i += k
#			print(ar[:b]+a+ar[i:])
			c= ar[:b]+a+ar[i:]
			break
		else:
			i += 1
	return c
	
for i in range(int(input())):
	flag =0
	ar,k = input().split()
	k =int(k)
	s = ar[:]
	j=0
#	print(s,k)
	while j<len(s):
#		print(s)
		if s == '+'*len(ar):
			print("Case #{}: {}".format(i+1,j))
			flag =1
			break
		s = flipper(s,k)
		j += 1
	if flag ==0:
		print("Case #{}: {}".format(i+1,"IMPOSSIBLE"))