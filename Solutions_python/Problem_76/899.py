#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

problem = 'C'
input_type = 'small'
id_ = '0'

in_file  = open(problem+'-'+input_type+'-'+id_+'.in', 'r')
out_file = open(problem+'-'+input_type+'-'+id_+'.out', 'w')

in_data = [line.rstrip() for line in in_file]
out_data = ''


ncases = int(in_data[0])
for j in range(1,ncases+1):
	n = int(in_data[2*j-1])
	candies = [int(k) for k in in_data[2*j].split(' ')]
	spl = 0
	res = -1
	while spl<2**n:
		sum1 = 0
		sum2 = 0
		s1 = -1
		s2 = -1
		for i in range(n):
			if (spl >> i) % 2 ==0:
				s1 = candies[i] if s1==-1 else s1^candies[i] 
				sum1 += candies[i]
			else:
				s2 = candies[i] if s2==-1 else s2^candies[i] 
				sum2 += candies[i]
		
		if s1==s2:
			res = max(res, sum1, sum2)
			#print s1,sum1,sum2
		spl = spl+1
	out_file.write("Case #" + str(j) + ": " + (str(res) if res>-1 else "NO") + '\n') 

in_file.close()
out_file.close()


