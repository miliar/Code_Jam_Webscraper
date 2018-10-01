#!/usr/bin/python

import sys

C=int(raw_input())

for case in range(C):
	row=raw_input().split()
	rs=int(row[0])
	cs=int(row[1])

	pict=[];
	for r in range(rs):
		rw=raw_input()
		pict.append(rw)

	
	imp=0;
	for r in range(rs):
		for c in range(cs):
			if pict[r][c]=='#':
				if r<(rs-1):
					if c<(cs-1):
						if (pict[r+1][c]=='#') and (pict[r][c+1]=='#')and (pict[r+1][c+1]=='#'):
							pict[r]=pict[r][:c]+'/\\'+pict[r][c+2:]
							pict[r+1]=pict[r+1][:c]+'\\/'+pict[r+1][c+2:]
						else:
							imp=1
							break;
					else:
						imp=1
						break;
				else:
					imp=1
					break;

	

	#print pict

	print('Case #'+str(case+1)+':')
	if imp:
		print('Impossible')
	else:
		for r in range(rs):
			print pict[r]

	#sys.stdout.write("Case #"+str(case+1)+": [")
	

