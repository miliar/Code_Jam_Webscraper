#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:11:35 2017

@author: ska
"""
T = int(input())
for i in range(1,T+1):
	d,n = map(int,input().split())
#	ar =[]
	t = 0
	for j in range(n):
		k,s = map(int, input().split())
		if t< (d-k)/s:
			t = (d-k)/s
			
	print("Case #{}: {}".format(i, d/t))