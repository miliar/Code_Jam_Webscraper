#!/usr/bin/python
from string import atoi
from sys import argv 

def solve(inputfile):
	f = open(inputfile, "r")
	cases = atoi(f.readline())	
	for c in range(cases):
		cdata = f.readline().split()	
		moves = atoi(cdata[0])
		cdata = cdata[1:]
		
		z = {"O":[],"B":[]}

		for m in range(moves):
			bot = cdata[m*2]
			spot = atoi(cdata[(m*2)+1])
			z[bot].append(spot)

		time = 0
		bd = {"O":[0,1], "B":[0,1]}
		for m in range(moves):
			bot = cdata[m*2]
			spot = atoi(cdata[(m*2)+1])
			t = (abs(bd[bot][1]-spot)+1) - (time - bd[bot][0])
			if t < 1:
				t = 1
			time += t

			bd[bot] = [time, spot]
		print "Case #%d: %d"%(c+1, time)
			
if __name__ == "__main__": solve(argv[1])
