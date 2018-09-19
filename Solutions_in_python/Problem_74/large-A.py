#! /urs/bin/python

from numpy import *
from decimal import *

f_in = open ('A-large.in','r')

f_out = open ('A-large.out','w')



N = int(f_in.readline())

for case in range(N):
	list=f_in.readline().split()
	print list
	p1=1
	p2=1
	n=int(list[0])
	a=zeros([n,2],int)
	for i in range(n):
		b=list[1+(2*i)]
		a[i][0]=int(ord(b)) #lettera colore robot
		a[i][1]=list[2+2*i] #posizione pulsante
	j=0
	k=0
	tt=0
	t=a[0][1]
	p1=a[0][1]
	td=t
	tt=t
	if size(a[:,0])==1:
		tt=a[0][1]
	print j,tt,td,p1,p2 
	while j<size(a[:,0])-1:
		while (a[j][0]==a[j+1][0]):
			t=abs(p1-a[j+1][1])+1
			tt=t+tt
			j=j+1
			td=t+td
			p1=a[j][1]
			if j+1==size(a[:,0]):
				break
			print j,tt,td,p1,p2 
		j=j+1

		if j==size(a[:,0]):
			break
		if td>=abs(p2-a[j][1]): # caso in cui l'altro robot e in posizione
			tt=1+tt
			td=1
		else:  #caso in cui l'altro robot non e in posizione
			tt=abs(p2-a[j][1])+1+tt-td
			td=abs(p2-a[j][1])+1-td
		t=0
		p2=p1
		p1=a[j][1]
		print j,tt,td,p1,p2 

	f_out.write ('Case #' + str(case+1) + ': '+str(tt)+'\n')

f_in.close()
f_out.close()
