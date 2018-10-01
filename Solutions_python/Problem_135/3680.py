#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def readrow(l):
	r=[]	
	for v in l.split(' '):		
		r.append(int(v))
	return r

def readboard(f):
	auxt=[]
	for i in range(4):
		line= f.readline().strip()
		auxt.append(readrow(line))		
	return auxt

afile = open(sys.argv[1], 'r')
T= int(afile.readline().strip())

for t in range(T):
	c1= int(afile.readline().strip())
	t1= readboard(afile)
	c2= int(afile.readline().strip())
	t2= readboard(afile)
	aux= [k for k in (t1[c1-1]) if k in (t2[c2-1])]	
	veces= len(aux)	
	if veces == 0:
		print "Case #"+str(t+1)+": Volunteer cheated!"
	elif veces == 1:
		print "Case #"+str(t+1)+":", aux[0]
	else:
		print "Case #"+str(t+1)+": Bad magician!"