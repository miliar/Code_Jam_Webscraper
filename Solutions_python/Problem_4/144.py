#!/usr/bin/python

import sys

def handle_case(v1,v2):
	n = len(v1)
	v1.sort()
	v2.sort()
	sum = 0
	for i in range(n):
		sum += v1[i]*v2[n-i-1]
	return sum

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		n = int(fsock.readline())
		v1 =  map(int,fsock.readline().rstrip("\n").split(" "))
		v2 =  map(int,fsock.readline().rstrip("\n").split(" "))
		print "Case #%d: %d" % (case, handle_case(v1,v2))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

