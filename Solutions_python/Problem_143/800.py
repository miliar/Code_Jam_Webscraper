# Gonzalo Ciruelos
# Problem B

import itertools
import copy



f = open('B-small-attempt0.in', 'r')
case_no = 1
for game in range(int(f.readline())):

	strings = []
	
	data = map(int, (f.readline()[:-1]).split(' '))
	
	a = data[0]
	b = data[1]
	k = data[2]
	
	result = 0
	for a_ in range(a):
		for b_ in range(b):
			if (a_&b_) < k:
				result+=1
	
	print 'Case #'+str(case_no)+': '+str(result)
	
	case_no+=1
