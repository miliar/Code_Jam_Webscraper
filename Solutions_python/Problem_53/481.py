# Andre Guedes (Brazil)
#
# Google Code Jam 2010.
#

import math

input_tuples = []

def parse_input():
	global input_tuples
	file = open('input.txt', 'r')
	lines = file.readlines()[1:]
	for line in lines:
		l = line.strip().split(' ')
		input_tuples.append((int(l[0]), int(l[1])))

def main():
	casenum = 1
	parse_input()
	for tuple in input_tuples:
		n = tuple[0]
		k  = tuple[1]
		if (k+1) % int(math.pow(2, n)):
			print 'Case #%d: OFF' % casenum
		else:
			print 'Case #%d: ON' % casenum
		casenum += 1

if __name__ == '__main__':
	main()
