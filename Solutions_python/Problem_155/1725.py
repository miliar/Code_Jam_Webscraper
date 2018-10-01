#!/usr/local/bin/python

import sys

def read_input(filepath):
	f = open (filepath, 'r')
	cases = f.readline()
	for x in xrange(1, int(cases)+1):	
		solve_prob(x, f.readline().rstrip())

def solve_prob(case, line):
	standing_up = 0
	result = 0
	max_shyness, data = line.split(' ')
	
	for i in xrange(int(max_shyness) + 1):
		shyness_level = i
		if standing_up < shyness_level:
			plus_friends = shyness_level - standing_up
			result += plus_friends
			standing_up += plus_friends

		standing_up += int(data[i])

	print "Case #%d: %d" % (case, result)
			

def main():
	if (len(sys.argv) < 2): 
		sys.exit("usage: blabla")

	read_input(sys.argv[1]) 


if __name__ == '__main__':
	main()