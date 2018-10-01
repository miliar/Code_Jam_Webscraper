#!/usr/bin/env python
# encoding: utf-8
"""
googjam1.py
Aditya
"""
import pdb
import sys
import getopt
from collections import defaultdict

def getOutput(g1, mat1, g2, mat2, case):
	p1 = set(mat1[g1])
	p2 = set(mat2[g2])
	l1 =[k for k in (set(p1) - (set(p1) - set(p2)))]
	l2 =[k for k in (set(p2) - (set(p2) - set(p1)))]
	print l1
	if(len(l1) >= 2):
		tout = "Case #"+str(case)+": Bad magician!"
	if(len(l1) == 0):
		tout = "Case #"+str(case)+": Volunteer cheated!"
	if (len(l1) == 1):
		tout = "Case #"+str(case)+": "+str(l1[0])
	return tout



def main():
	fname = sys.argv[1]
	#pdb.set_trace()
	numcases = 0
	count = 0
	innloop = 0
	fh = open(fname, 'r')
	outname = "/Users/adityajitta/Desktop/output1.txt"
	fh1 = open(outname, 'w')
	for l in fh:
		if (count == 0):
			tl = l.strip()
		if (count > 0):
			l=l.strip()
			if(innloop == 0):
				numcases +=1
				arg1 = int(l.strip())
				arg2 = defaultdict(list)
			if (len(l.strip()) > 1 and innloop < 5):
				arg2[innloop] = map(int,l.strip().split())
			if(innloop == 5):
				arg3 = int(l.strip())
				arg4 = defaultdict(list)
			if (len(l.strip()) > 1 and (5 < innloop < 10)):
				arg4[innloop-5] = map(int,l.strip().split())
			innloop += 1
			if (innloop == 10):
				out_txt = getOutput(arg1,arg2,arg3,arg4, numcases)
				print >>fh1, out_txt
				#pdb.set_trace()
				innloop = 0
		count += 1
	fh.close()
	fh1.close()


main()
