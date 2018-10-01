#!/usr/bin/python
import sys
from pprint import pprint

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')
	for case in xrange(1, int(infile.readline())+1):
		e, n = (int(number) for number in infile.readline().split())
		existing = {}
		
		for i in xrange(e):
			old = existing
			for dir in infile.readline()[1:].split("/"):
				if not dir.strip() in old:
					old[dir.strip()] = {}
				old = old[dir.strip()]
		
		mkdirs = 0
		for i in xrange(n):
			old = existing
			for dir in infile.readline()[1:].split("/"):
				if not dir.strip() in old:
					old[dir.strip()] = {}
					mkdirs+=1
				old = old[dir.strip()]
		
		
		outfile.write("Case #%i: %i\n"%(case, mkdirs))

if __name__ == "__main__":
	main()
