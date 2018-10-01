# -*- coding: utf-8 -*-
# @Author: Patrice Béchard 20019173
# @Date:   2017-04-07 21:01:30
# @Last Modified time: 2017-04-07 21:59:41
#
# Tidy Numbers
# 

def is_tidy(number):
	listNumber = list(number)
	for i in reversed(range(1,len(number))):
		if int(listNumber[i]) < int(listNumber[i-1]):
			listNumber[i-1] = str(int(listNumber[i-1])-1)
			for j in range(i,len(number)):
				listNumber[j] = str(9)
	number = ''.join(listNumber)
	return number

file = 'B-large.in'
file2 = 'output2.txt'
f = open(file)
g = open(file2,'w')

nCase = int(f.readline().strip())

for i in range(nCase):
	number = f.readline().strip()
	number = int(is_tidy(number))

	out = 'Case #%d: %d\n'%(i+1,number)
	g.write(out)
