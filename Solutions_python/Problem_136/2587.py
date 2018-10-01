from __future__ import division
import string
import sys

def calTime(C,F,X,count):
	S = 2
	time = 0
	while(1):
		if C*(F + S) > X*F:
			time += X/S
			print 'Case #%r: %.7f' % (count,time)
			return
		else:
			time += C/S
			S += F
			

def parseline(line):
	return line.rstrip().split(' ')

if __name__ == "__main__":
	if len(sys.argv) == 1:
		fin = open('input.txt')
	else:
		fin = open(sys.argv[1])
	count = string.atoi(fin.readline().rstrip())

	count = 1
	for line in fin:
		data =  parseline(line)
		C = string.atof(data[0])
		F = string.atof(data[1])
		X = string.atof(data[2])
		calTime(C,F,X,count)
		count += 1

		
