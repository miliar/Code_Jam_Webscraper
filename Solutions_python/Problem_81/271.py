#!/usr/bin/python

import sys

f = open("a.in","rb")
t = int(f.readline())

def toi(t):
	if (t=='1'):
		return 1
	else:
		return 0

for i in range(t):
	n = int(f.readline())
	m = []
	w = []
	ow = []
	oow = []
	for ii in range(n):
		m.append(f.readline())
		a,b = 0,0
		for jj in range(n):
			if (m[ii][jj]!='.'):
				a+= toi(m[ii][jj])
				b+=1
		w.append([a,b])
	
	for ii in range(n):
		s = 0.0
		for jj in range(n):
			if (m[ii][jj]!='.'):
				a= w[jj][0]-1+int(m[ii][jj])
				b=w[jj][1]-1
				s+=float(a)/b
		ow.append(s/w[ii][1])

	for ii in range(n):
		s = 0.0
		for jj in range(n):
			if (m[ii][jj]!='.'):
				s+=ow[jj]
		oow.append(s/w[ii][1])

	print "Case #"+str(i+1)+":"
	for ii in range(n):
		print (0.25*w[ii][0]/w[ii][1] + 0.5*ow[ii] + 0.25*oow[ii])
