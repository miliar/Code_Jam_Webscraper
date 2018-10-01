# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/env python
import sys
import random
import numpy as np
from time import time
import math
def flipper(cakes,k):
	flag = False
	if k > len(cakes):
		for i in range(len(cakes)):
			#print(cakes[i])
			if cakes[i] != '+':
				return (False, 0)
	currindex = 0
	while(flag == False and currindex < len(cakes)-k+1):
		if cakes[currindex]=='-':
			flag = True
		else:
			currindex += 1

	if flag == True:
		for q in range(k):
			if cakes[currindex + q] == '-':
				cakes = cakes[:currindex + q] + "+" + cakes[currindex+q+1:]
				
			elif cakes[currindex + q] == '+':
				cakes = cakes[:currindex + q] + "-" + cakes[currindex+q+1:]

		(lateflag, num) = flipper(cakes[currindex+1:], k)
		return(lateflag, num+1)
	else:
		for i in range(len(cakes)):
			if cakes[i] != '+':
				return (False, 0)
		return (True, 0)

n = int(raw_input().strip())
for i in range(n):
	raw = raw_input().strip().split(' ')
	cake = str(raw[0])
	flip = int(raw[1])
	#print(cake)
	#print(flip)
	#print(flipper(cake,flip))
	(res, num) = flipper(cake,flip)
	outputstr = "Case #" + str(i+1) + ": "
	if res == False:
		outputstr = outputstr + "IMPOSSIBLE"
	else:
		outputstr = outputstr + str(num)
	print(outputstr)

