#from __future__ import division
import itertools
from fractions import gcd
from math import *
from bisect import bisect_left , bisect_right
import heapq
from collections import deque , defaultdict , Counter
from itertools import combinations as C
from random import randrange as rd
def Ls():
	return list(raw_input())
def get(a):
	return map(a , raw_input().split())
def Int():
	return int(raw_input())
def Str():
	return raw_input()

###REDIRECT IO
import sys
sys.stdin = open('B-small-attempt0.in' ,'r')
#sys.stdin = open('A-large-attempt0.in' ,'r')
#sys.stdin = open('A-small-practice.in' ,'r')

sys.stdout = open('output.txt' , 'w')
###

#may the force with me.

for x in xrange(input()):
	n , r , o , y , g , b , v = get(int)
	ls = [0]*n
	print 'Case #%d:' % (x+1) ,
	if max(r,y,b) == r:
		if max(r,y,b) > (n)/2:
			print 'IMPOSSIBLE'
			continue
		if min(y,b) == b:
			for i in xrange(0,n,2):
				if r > 0:
					ls[i] = 1
					r -= 1
			for i in xrange(0,n,2):
				if ls[i] == 0:
					ls[i] = 3
					b -= 1
			for i in xrange(1,n,2):
				if ls[i] == 0 and b > 0:
					ls[i] = 3
					b -= 1
				if ls[i] == 0:
					ls[i] = 2
		elif min(y,b) == y:
			for i in xrange(0,n,2):
				if r > 0:
					ls[i] = 1
					r -= 1
			for i in xrange(0,n,2):
				if ls[i] == 0:
					ls[i] = 2
					y -= 1
			for i in xrange(1,n,2):
				if ls[i] == 0 and y > 0:
					ls[i] = 2
					y -= 1
				if ls[i] == 0:
					ls[i] = 3
	elif max(r,y,b) == y:
		if max(r,y,b) > (n)/2:
			print 'IMPOSSIBLE'
			continue
		if min(r,b) == r:
			for i in xrange(0,n,2):
				if y > 0:
					ls[i] = 2;
					y -= 1
			for i in xrange(0,n,2):
				if ls[i] == 0:
					ls[i] = 1
					r -= 1
			for i in xrange(1,n,2):
				if ls[i] == 0 and r > 0:
					ls[i] = 1
					r -= 1
				if ls[i] == 0:
					ls[i] = 3
		elif min(r,b) == b:
			for i in xrange(0,n,2):
				if y > 0:
					ls[i] = 2
					y -= 1
			for i in xrange(0,n,2):
				if ls[i] == 0:
					ls[i] = 3
					b -= 1
			for i in xrange(1,n,2):
				if ls[i] == 0 and b > 0:
					ls[i] = 3	
					b -= 1
				if ls[i] == 0:
					ls[i] = 1
	else:
		if max(r,y,b) > (n)/2:
			print 'IMPOSSIBLE'
			continue
		if min(r,y) == r:
			for i in xrange(0,n,2):
				if b > 0:
					ls[i] = 3
					b -= 1
			for i in xrange(0,n,2):
				if ls[i] == 0:
					ls[i] = 1
					r -= 1
			for i in xrange(1,n,2):
				if ls[i] == 0 and r > 0:
					ls[i] = 1;r -=1
				if ls[i] == 0:
					ls[i] = 2
		elif min(y,r) == y:
			for i in xrange(0,n,2):
				if b > 0:
					ls[i] = 3
					b -= 1
			for i in xrange(0,n,2):
				if ls[i] == 0:
					ls[i] = 2
					y -= 1
			for i in xrange(1,n,2):
				if ls[i] == 0 and y > 0:
					ls[i] = 2;y-=1
				if ls[i] == 0:
					ls[i] = 1
	sts = []	
	for i in ls:
		if i == 1:sts.append('R')
		elif i == 2:sts.append('Y')
		else:sts.append('B')
	print ''.join(sts)
		
			
			
	
	
	
		
			
			
		
