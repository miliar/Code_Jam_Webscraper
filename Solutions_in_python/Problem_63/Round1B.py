'''
Codejam template

@author: alarobric
'''

import math

def solve():
	print
	global l, p, c
	l, p, c = [int(z) for z in infile.readline().split()]
	print "l, p, c", l, p, c
	
	mult = 0
	while l < p:
		l *= c
		mult += 1
	print mult
	if mult == 1:
		return 0
	return int(math.ceil(math.log(mult, 2)))
	return int(math.ceil(math.sqrt(mult)))
	
filepath = '/home/alan/Downloads/'
fileprefix = 'B-test' #Change me!
fileprefix = 'B-small-attempt1'
fileprefix = 'B-large'

infilename = filepath + fileprefix + '.in'
outfilename = filepath + fileprefix + '.out'
infile = open(infilename, 'rU')
outfile = open(outfilename, 'w+')

numCases = int(infile.readline())
print numCases

for case in range(1, numCases+1):
	str = "Case #%d: %s" %(case, solve())
	print str
	outfile.write(str + "\n")

infile.close()
outfile.close()
