# 

import math
import Queue
import copy

def main():
	# fp = open('a.in')
	fp = open('A-small-attempt0.in')
	# fp = open('A-large.in')

	for case in xrange(int(fp.readline())):
		r, t = map(int, fp.readline().split())

		result = int(((1-2*r) + math.sqrt((-1+2*r) * (-1+2*r)+8*t)) / 4)

		print 'Case #{0}: {1}'.format(case+1, result)

if __name__ == "__main__":
	main()
