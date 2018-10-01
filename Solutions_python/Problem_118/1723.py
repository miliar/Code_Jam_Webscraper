# Fair and square

import math
import sys

def fas(a, b):
	il = int(math.floor(math.sqrt(a)))
	ir = int(math.ceil(math.sqrt(b)))
	ctr = 0

	for i in range(il, ir+1):
		if str(i) == str(int(str(i)[::-1])):
			if str(i**2) == str(int(str(i**2)[::-1])):
				if i**2 >= a and i**2 <= b:
					ctr += 1

	return ctr

with open(sys.argv[1], 'r') as f:
	n = int(f.readline().strip())
	for i in range(n):
		l = f.readline().strip().split()
		a = int(l[0])
		b = int(l[1])
		print "Case #%d: %d" % (i+1, fas(a,b))
		