#!/usr/bin/python

import sys

C=int(raw_input())

for case in range(C):
	row=raw_input().split()
	N=int(row[0])
	L=int(row[1])
	H=int(row[2])

	row=raw_input().split()
	a=map(int,row)

	res=0
	for i in range(L,H+1):
		can=True
		for j in range(N):
			if i%a[j]!=0:
				if a[j]%i!=0:
					can=False
					break
		if can:
			res=i
			break


	if res==0:
		print('Case #'+str(case+1)+': NO')
	else:
		print('Case #'+str(case+1)+': '+str(res))

	#sys.stdout.write("Case #"+str(case+1)+": [")
	

