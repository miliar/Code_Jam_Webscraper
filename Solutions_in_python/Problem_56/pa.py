#!/usr/bin/env python
import math
import sys
import os
from os import system

def counting(row,K):
	R = 0
	B = 0
	count = {}
	prevword = ''
	count['R'] = 0
	count['B'] = 0
	for word in row:
		if word == prevword:
			count[word] = count[word] + 1
			if count['R'] >= K:
				R = 1
				#print 'R'
				#print row
			if count['B'] >= K:
				B = 1
				#print 'B'
				#print row
		else :
			count[word] = 1
		prevword = word
	
	return R,B


R = 0
B = 0

fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	R = 0
	B = 0
	l = fp.readline().split()
	N = int(l[0])
	K = int(l[1])
	board = []
	for j in range(N):
		l = fp.readline()
		t = []
		v = []
		for k in range(N):
			if l[k] != '.':
				t.append(l[k])
			else :
				v.append('.')
		t.reverse()
		board.append(t+v)
	col = []
	coll = []
	colr = []
	for j in range(N):
		col.append([])
		coll.append([])
		coll.append([])
		colr.append([])
		colr.append([])
	k = 0
	for row in board:
		count = {}
		prevword = ''
		count['R'] = 0
		count['B'] = 0
		j = 0
		for word in row:
			if word == prevword:
				count[word] = count[word] + 1
				if count['R'] >= K:
					R = 1
					#print 'R'
					#print row
				if count['B'] >= K:
					B = 1
					#print 'B'
					#print row
			else :
				count[word] = 1
			prevword = word
			col[j].append(word)
			coll[N-1+k-j].append(word)
			colr[k+j].append(word)
			j = j + 1
		k = k + 1
	#print R
	#print B
	#print "col\n"
	#print col
	#print "coll\n"
	#print coll
	#print "colr\n"
	#print colr
	for j in range(N):
		RR,BB = counting(col[j],K)
		if RR > R:
			R = RR
		if BB > B:
			B = BB
	for j in range(2*N):
		RR,BB = counting(coll[j],K)
		if RR > R:
			R = RR
		if BB > B:
			B = BB
		RR,BB = counting(colr[j],K)
		if RR > R:
			R = RR
		if BB > B:
			B = BB
	#print B
#	print R

	fout.write('Case #%d: '%(i+1))
	if R == 1:
		if B == 1:
			fout.write('%s\n'%("Both"))
		else :
			fout.write('Red\n')
	else :
		if B == 1:
			fout.write('Blue\n')
		else :
			fout.write('Neither\n')
