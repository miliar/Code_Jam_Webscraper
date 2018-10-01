import math
from math import *

#fname = "test"
fname = "A-large"

ifile = open(fname + '.in', 'r')
ofile = open(fname + '.out', 'w+')

with ifile:
	num_case = ifile.readline()
	i = 0
	for line in ifile:
		sumtmp = 0
		friend = 0
		i = i + 1
		list_int = [int(x) for x in line.split()]
		smax = list_int[0]
		s = []
		for j in range(0, smax+1):
			if j > sumtmp and j-sumtmp > friend:
				friend = j - sumtmp
			s.append(math.floor((list_int[1]%(10**(smax-j+1)))/(10**(smax-j))))
			sumtmp = sumtmp + s[j]
		print "Case #%d: %d" % (i, friend)
		ofile.write("Case #%d: %d\n" % (i, friend))
