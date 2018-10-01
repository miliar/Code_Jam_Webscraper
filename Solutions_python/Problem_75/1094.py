#!/usr/bin/python

import sys

C=int(raw_input())

for case in range(C):
	row=raw_input().split()
	combines=int(row[0])

	comb={}
	for i in range(combines):
		st=row[i+1]
		comb[st[0]]=[st[1],st[2]]
		comb[st[1]]=[st[0],st[2]]

	oposites=int(row[combines+1])
	op={}
	for i in range(oposites):
		st=row[combines+i+2]
		op[st[0]]=st[1]
		op[st[1]]=st[0]

	seq=row[combines+oposites+3]

	res=[]

	for c in seq:
		if len(res)>0:
			if c in comb.keys():
				if comb[c][0]==res[len(res)-1]:
					res[len(res)-1]=comb[c][1]
					continue
			if c in op.keys():
				if res.count(op[c])>0:
					res=[]
					continue
		res.append(c)

	sys.stdout.write("Case #"+str(case+1)+": [")
	first=True
	for c in res:
		if not first:
			sys.stdout.write(', ')

		first=False
		sys.stdout.write(c)

	print ']'
	#sys.stdout.write(']')

