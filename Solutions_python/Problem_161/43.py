#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import *
#from sets import *
import math
import sys

if __name__ == "__main__":
	t = int(input())
	for caseIdx in range(1,t+1):
		sys.stdout.flush()
		n= int(input())
		tree = []
		for i in range(n):
			x, y = map(int, input().split(' '))
			tree.append((x,y))

		ans = []
		for i in range(0, len(tree)):
			logging = n
			for j in range(0, len(tree)):
				if j == i:
					continue
				positive = 0
				negative = 0
				for k in range(0, len(tree)):
					result = (tree[j][1]-tree[i][1])*tree[k][0] - (tree[j][0]-tree[i][0])*tree[k][1]+(tree[j][0]*tree[i][1]-tree[i][0]*tree[j][1])
					#print(i,j,k, result)
					if result>0:
						positive = positive + 1
					elif result<0:
						negative = negative + 1
				logging = min(logging, min(positive, negative))
			ans.append(logging)

		if n == 1:
			ans = [0]
		print("Case #%d:" % (caseIdx))
		for a in ans:
			print(a)
