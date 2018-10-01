#!/usr/bin/python

import sys
import math

numbers=[]
for i in range(0,10**7+100000):
	num=i*i
	s=str(num)
	s2=str(i)
	if str(num)==''.join(reversed(s)) and s2==''.join(reversed(s2)):
		numbers.append(num)

if 1==1:#sys.stdin.readline().rstrip("\n")=='Input':
	count = int(sys.stdin.readline(),10)
	for i in range(0,count):
		line=sys.stdin.readline().rstrip("\n")
		ar=line.split()
		a=int(ar[0],10)
		b=int(ar[1],10)
		res=0	
		for el in numbers:
			if el>=a and el<=b:
				res=res+1
		
		print("Case #"+str(i+1)+": "+str(res))
		

#End
