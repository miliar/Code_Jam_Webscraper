#!/usr/bin/python

import sys
import math	
from datetime import datetime

startTime = datetime.now()
sys.setrecursionlimit(20000)

def readn(n):
	return [raw_input().strip() for i in range(n)]
def read():
	return raw_input()
def readints():
	return map(int, read().split())
def wl(n, o):
	print("Case #{0}: {1}".format(n, o))

def getCh(s, ch):
	cc = 0
	for c in s:
		if c == ch: cc+=1
	return cc
	
T = int(read())
for TT in range(T):
	N = readints()[0]
	data = readn(N)
	_0 = [0]*N
	_1 = [0]*N
	WP=[0]*N
	OWP=[0]*N
	OOWP=[0]*N
	for i in range(N):
		_0[i] = getCh(data[i], '0')
		_1[i] = getCh(data[i], '1')
		WP[i] = (_1[i] + 0.0) / (_0[i]+_1[i])
	for i in range(N):
		ss = 0.0
		cnt = 0
		for j in range(N):
			if data[i][j] == '1':
				ss += (_1[j] + 0.0) / (_0[j]+_1[j] - 1.0)
				cnt += 1
			elif data[i][j] == '0':
				ss += (_1[j] - 1.0) / (_0[j]+_1[j] - 1.0)
				cnt += 1
		OWP[i]=ss / cnt
	for i in range(N):
		ss = 0.0
		cnt = 0
		for j in range(N):
			if data[i][j] != '.':
				ss += OWP[j]
				cnt += 1
		OOWP[i] = ss / cnt
	wl(TT+1, "")
	for i in range(N):
		print (0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i])
	
	
	
#print(datetime.now()-startTime)