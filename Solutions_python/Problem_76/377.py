#!/usr/bin/python
from string import atoi
from sys import argv 
import math

def runtree(select, pos, level):
	if level == 20:
		return True

	works = False	
	for y in pos[level]:
		if y in select:
			if not runtree(select, pos, level+1):
				select.remove(y)
			else:
				works = select 
	
	if not pos[level]:
		works = runtree(select, pos, level+1)

	print level, works
	return works
	

def solve(inputfile):
	f = open(inputfile, "r")
	cases = atoi(f.readline())	
	for case in range(cases):
		f.readline()
		cdata = f.readline()
		cdata = cdata.split()
		cd = []
		total = 0
		for n in cdata:
			cd.append(atoi(n))
			total = total^atoi(n)
		

		if total != 0:
			output = "NO"

		else:
			cd.sort()
			output  = 0
			for v in cd[1:]:
				output += v 

		print "Case #%d: %s"%(case+1, output)

if __name__ == "__main__": solve(argv[1])
