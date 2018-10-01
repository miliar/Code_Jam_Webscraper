# -*- coding: utf-8 -*-
from math import *
import re

fin = open("A-large.in")
fout = open("A-large.out","w")

cases= int(fin.readline().split()[0])
case = 0

def answer(x):
	global case, cases
	case += 1
	print >>fout, "Case #"+str(case)+": "+str(x)
	print "Case #"+str(case)+": "+str(x)
	
for test in xrange(cases):
	n = int(fin.readline().split()[0])
	played=[0]*n
	lost=[[]]*n
	won=[[]]*n
	for i in xrange(n):
		aux=fin.readline()
		for j in xrange(n):
			if (aux[j]!='.'): played[i]+=1
			if (aux[j]=='0'): lost[i]=lost[i]+[j]
			if (aux[j]=='1'): won[i]=won[i]+[j]
	wp=[0.0]*n
	for i in xrange(n):
		wp[i]=float(len(won[i]))/played[i]
	print wp
	owp=[0.0]*n
	for i in xrange(n):
		for j in won[i]:
			owp[i]+=float(len(won[j]))/(played[j]-1)
		for j in lost[i]:
			owp[i]+=float(len(won[j])-1)/(played[j]-1)
		owp[i]=owp[i]/(len(lost[i])+len(won[i]))
	print owp
	oowp=[0.0]*n
	for i in xrange(n):
		for j in won[i]:
			oowp[i]+=owp[j]
		for j in lost[i]:
			oowp[i]+=owp[j]
		oowp[i]=oowp[i]/(len(lost[i])+len(won[i]))
	print oowp
	rpi=[0.0]*n
	for i in xrange(n):
		rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]
	res="\n"
	for i in xrange(n):
		res+="%f\n" % (rpi[i])
	answer(res[:-1])	
	
	
	
	
	
	
	
	
	
	
	
	
	


