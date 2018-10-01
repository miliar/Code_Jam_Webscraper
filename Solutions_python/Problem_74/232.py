#! /usr/bin/env python
# -*- coding: UTF-8 -*-
	
''' Bot Trust
'''

import sys

if len(sys.argv) <= 1:
	exit('args!')
fn = sys.argv[1]
fc = open(fn).readlines()

v = False
if '-v' in sys.argv:
	v = True

T = int(fc[0])

def robot(oX,X,xrder):
	if oX:
		if oX[-1][1] == X and xrder[-1] == oX[-1]:
			if v: print 'Push button %i \t'%(X),
			oX.pop()
		elif oX[-1][1] > X:
			X+=1
			if v: print 'Move to button %i\t'%(X),
		elif oX[-1][1] < X:
			X-=1
			if v: print 'Move to button %i\t'%(X),
		else:
			if v: print 'Stay at button %i\t'%(X),
	else:
		if v: print 'Stay at button %i\t'%(X),
	return X

for i in range(T):
	l = fc[i+1].strip().split(' ')
	N = l[0]
	order = [ (l[j],int(l[j+1]),j) for j in range(1,len(l[1:]),2) ][::-1]
	oO,oB = [ j for j in order if j[0]=='O' ],[ j for j in order if j[0]=='B' ]
	
	O,B = 1,1
	
	t=0
	cur = order[0]
	if v: print "Time\t| Blue             \t| Orange"
	if v: print "--------+-------------------+-----------------"
	while True:
		t+=1
		if v: print "  %i \t|"%t,
		B = robot(oB,B,order)
		if v: print "|",
		O = robot(oO,O,order)
		if v: print
		if order and ((oB and order[-1]!=oB[-1]) or not oB) and ((oO and order[-1]!=oO[-1]) or not oO):
			order.pop()
		if not order:
			break
	
	print( 'Case #%i: %i'%(i+1,t) )
