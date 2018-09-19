#!/usr/bin/env python
import math
import sys
import os
from os import system


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	cell = []
	bac = []
	R = int(fp.readline())
	max = 0
	for j in range(R):
		l = fp.readline()
		kk = []
		for k in l.split():
			kk.append(int(k))
			if int(k) > max:
				max = int(k)
		bac.append(kk)
	max = max + 1
	for j in range(max):
		cell.append([0]*max)
	while len(bac) > 0:
		temp = bac.pop()
		j = temp[0]
		while j <= temp[2]:
			k = temp[1]
			while k <= temp[3]:
				cell[k-1][j-1] = 1
				k = k + 1
			j = j + 1
	#print cell
	
	summ = 0
	for c in cell:
		summ = summ + sum(c)
	num = 0
	while summ > 0:
		cell2 = []
		for j in range(max):
			cell2.append([0]*max)
		for x in range(max):
			for y in range(max):
				if cell[x][y] == 1:
					if cell[x-1][y] == 0 and cell[x][y-1] == 0:
						cell2[x][y] = 0
					else :
						cell2[x][y] = 1
				if cell[x][y] == 0:
					if cell[x-1][y] == 1 and cell[x][y-1] == 1:
						cell2[x][y] = 1
					else :
						cell2[x][y] = 0
		cell = cell2
		num = num + 1
		#print num,cell
		summ = 0
		for c in cell:
			summ = summ + sum(c)
	fout.write('Case #%d: %d\n'%(i+1,num))
