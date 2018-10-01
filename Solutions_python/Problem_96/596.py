#!/usr/bin/env python
import sys
import re
import urllib
import math
import os
from timeit import Timer

#def subset = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

def output(case, answer):
	return "Case #%d: %d\n" % (case, answer)

def func(n):
	if n == 0: return 0
	if n == 1 or n == 2: return 1
	if n % 3 == 0: return n/3
	else: return int(math.floor(float(n)/3)) + 1

def determine(l,s,p):
	total = 0
	maxnorm = [func(val) for val in l]
	candidates = len([val for index, val in enumerate(maxnorm) if val == p-1 and l[index] % 3 != 1 and l[index] > 1])
	while candidates and s:
		total += 1
		candidates -= 1
		s -= 1
	total += len([val for val in maxnorm if val >= p])
	return total
	
def main(filein, fileout):
	case = 0
	f = open(filein, 'r')
	o = open(fileout, 'w')
	times = int(f.readline())
	while case < times:
		answer = 0
		values = f.readline().split(" ")
		numPlayers = int(values[0])
		surprising = int(values[1])
		limit = int(values[2])
		values = [int(number) for number in values[-numPlayers:]]
		answer = determine(values,surprising,limit)
		case += 1
		o.write(output(case, answer))
	f.close()
	o.close()

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[1][:-2]+'out')
