#!/usr/bin/python
#
# stjepan.henc@fer.hr
#

import math

T = int(input())


for i in range(T):
	ulaz = input()
	ulaz = ulaz.split(' ')
	N = int(ulaz[0])
	S = int(ulaz[1])
	p = int(ulaz[2])
	t = [int(x) for x in ulaz[3:len(ulaz)]]
	
	tot = 0
	
	for G in t:
		
		if (G == 0):
			if (math.floor(G/3) >= p):
				tot += 1
		elif (G%3 == 0):
			if (math.floor(G/3) >= p):
				tot += 1
			elif (S > 0):
				if (math.floor(G/3) + 1 >= p):
					tot += 1
					S -= 1
		elif (G%3 == 1):
			if (math.floor(G/3) + 1 >= p):
				tot += 1
		else: 
			if (math.floor(G/3) + 1 >= p):
				tot += 1
			elif (S > 0):
				if (math.floor(G/3) + 2 >= p):
					tot += 1
					S -= 1
				
	print("Case #" + str(i + 1) + ":", tot)	

