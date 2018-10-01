# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/env python
import sys
import random
import numpy as np
from time import time
import math

def process(x):
	numlist = list(str(x))
	#check if we're done

	flag = False
	currIndex = 0
	while(flag == False and currIndex < len(numlist)-1):
		if numlist[currIndex] > numlist[currIndex + 1]:
			flag = True
		else:
			currIndex += 1
	if flag == True:
		while(currIndex > 0 and numlist[currIndex] == numlist[currIndex - 1]):
			currIndex -= 1



		if numlist[currIndex+1] == 0:
			numlist[currIndex] = ""
			for x in range (currIndex+1, len(numlist)):
				numlist[x] = "9"
		else:
			numlist[currIndex] = str(int(numlist[currIndex])-1) 
			for x in range (currIndex+1, len(numlist)):
				numlist[x] = "9"


		output = int(''.join(numlist))
	else:
		output = x
	return(output)

n = int(raw_input().strip())
for i in range(n):
	x = int(raw_input().strip())
	outputstr = "Case #" + str(i+1) + ": " + str(process(x))
	print(outputstr)