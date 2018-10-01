import itertools
from fractions import gcd
from math import sqrt
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
sys.stdin = open('input.txt' ,'r')
sys.stdout = open('output.txt' , 'w')
###

#SHIT GOES BELOW
#when you can't do recursion with python ^_^
#lets take risk , dobara likhne ka mood nhi , 10**8 iteration python 4 min haye...

def solve(n,k):
	ls = []
	st = n - 1
	if (st % 2 == 1):
		put = (st/2 , st/2+1)
	else:
		put = (st/2 , st/2)
	queue = deque([put])
	while queue:
		node = queue.popleft()
		#print node
		ls.append(node)
		if (node > (0,0)):
			stx = node[0] - 1
			if (stx % 2 == 1):
				putx = (stx/2 , stx/2+1)
			else:
				putx = (stx/2 , stx/2)
			sty = node[1] - 1
			if (sty % 2 == 1):
				puty = (sty/2 , sty/2+1)
			else:
				puty = (sty/2 , sty/2)
			if (putx >= (0,0)):queue.append(putx)
			if (puty >= (0,0)):queue.append(puty)
	ls.sort(reverse = True)
	#print ls
	a,b = max(ls[k-1]),min(ls[k-1])
	return str(a) + " " + str(b)
	
def logme(n,k):
	seq = []
	while k > 1:
		seq.append(k)
		k /= 2
	#print seq
	st = n - 1
	if (st % 2 == 1):
		put = (st/2+1 , st/2)
	else:
		put = (st/2 , st/2)
	for i in seq:
		if i % 2 == 0:
			st = put[0] - 1
		else:	st = put[1] - 1
		if (st % 2 == 1):
			put = (st/2 + 1, st/2)
		else:
			put = (st/2 , st/2)
	a , b = put
	return str(a) + " " + str(b)
		
T = input()
for _ in xrange(T):
	n , k = get(int)
	print "Case #%s:" %(_+1),logme(n,k)
	#print logme(n,k)

		
