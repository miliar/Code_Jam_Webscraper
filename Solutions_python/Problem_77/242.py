#! /usr/bin/env python
# -*- coding: UTF-8 -*-
	
''' D - Goro Sort
'''

import sys, math, random

if len(sys.argv) <= 1:
	exit('args!')
fn = sys.argv[1]
fc = open(fn).readlines()

v = False
if '-v' in sys.argv:
	v = True

T = int(fc[0])

def goro1(Ns,sNs,Nsi):
	c = 0
	for j in range(len(Ns)):
		while Ns[j] != sNs[j]:
			# if lsti[ lst[lsti[lst[j]][0]] ][0] == j: # clean switch
			w2 = Ns[Nsi[Ns[j]][0]]
			Ns[Nsi[Ns[j]][0]] = Ns[j]
			Nsi[Ns[j]].pop(0)
			Ns[j] = w2
			c += 2
		else:
			''#i the right place
	return c

def goro2(Ns,sNs,Nsi):
	c = 0
	while Ns != sNs:
		m1,m2 = [],[]
		for i in range(len(Ns)):
			if Ns[i] != sNs[i]:
				m1.append(i)
				m2.append(i)
		if m1:
			c += 1
			random.shuffle(m1)
			for m in range(len(m2)):
				m1[m] = Ns[m1[m]]
			for m in range(len(m2)):
				Ns[m2[m]] = m1[m]
	return c

def goro3(Ns,sNs,Nsi):
	c = 0
	for i in range(len(Ns)):
		if Ns[i] != sNs[i]:
			c += 1
	return c

for i in range(0,T*2,2):
	l1 = fc[i+1].strip()
	l2 = fc[i+2].strip().split(' ')
	
	N = int(l1)
	Ns = [ int(n) for n in l2 ]
	
	sNs = sorted(Ns)
	Nsi = {}
	
	for j in range(len(sNs)):
		if not sNs[j] in Nsi:
			Nsi[sNs[j]] = []
		Nsi[sNs[j]].append(j)
	
	c = goro3(Ns,sNs,Nsi)
	
	#assert (Ns==sNs), '%i Not sorted right ! %s'%(i+2,Ns)
	
	print 'Case #%i: %f'%(i/2+1,c)
