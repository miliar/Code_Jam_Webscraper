#!/usr/bin/python
import sys

def mainfunc():
	f = open("input.txt", "r")
	i = int(f.readline().strip())
	j = 0
	while (j < i):
		ll = list(f.readline().strip().split())
		gl = int(ll[0])
		up = int(ll[1])
		p = int(ll[2])
		scores = [int(x) for x in ll[3:]]
		count = 0;
		for el in scores:
			if (p > 1):
				if (el > 3*(p - 1)):
					count += 1
				elif (el > 3*p - 5) and (up > 0):
					count += 1
					up -= 1
			else:
				if (p == 1):
					if (el > 0):
						count += 1
				else:
					count += 1
				
		print "Case #%d: %d" % (j+1, count)
		j += 1
	
if __name__ == "__main__":
	mainfunc()
