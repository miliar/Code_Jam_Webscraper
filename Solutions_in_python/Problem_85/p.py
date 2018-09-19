#!/usr/bin/python

import sys

C=int(raw_input())

for case in range(C):
	row=raw_input().split()
	L=int(row[0])
	t=int(row[1])
	N=int(row[2])
	C=int(row[3])
	a=map(int,row[4:])

	suma=sum(a)
	time=((N/C)*suma+sum(a[:N%C]))*2

	Cs=t/(suma*2)	#Cs without boost
	t=t-Cs*suma*2
	Cr=N/C-(Cs+1)	#remaining Cs

	remain=a[:N%C] 	#one Cs remain
	for i in range(C):
		if t<=(2*a[i]):
			remain.append(a[i]-t/2.0)

		t=t-2*a[i]
		if t<0:
			t=0

	remain=sorted(remain)
	a=sorted(a)
	
	while L>0:
		if len(a)>0:
			aa=a.pop()
			if L>Cr:
				time=time-aa*Cr
				L=L-Cr
			else:
				time=time-aa*L
				break
		else:
			aa=0

		if len(remain)>0:
			if len(a)>0:
				if remain[-1]>a[-1]:
					time=time-remain.pop()
					L=L-1
			else:
				time=time-remain.pop()
				L=L-1



	print('Case #'+str(case+1)+': '+str(int(time)))

	#sys.stdout.write("Case #"+str(case+1)+": [")
	

