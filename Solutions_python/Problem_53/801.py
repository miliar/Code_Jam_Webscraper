#!/usr/bin/env python
import sys

filename = sys.argv[1]
fp = open(filename)
input = [line for line in fp]
fp.close()

inum = int(input[0])
for i in range(1,inum+1):
	case = input[i]
	line = case.split()
	n = int(line[0])
	k = int(line[1])
	exp = 2**n
	if k < 1 or k+1 < exp:
		output = "OFF"
	else:
		output = "ON" if (k+1)%exp==0 else "OFF"
	print "Case #%s: %s" %(i,output)
