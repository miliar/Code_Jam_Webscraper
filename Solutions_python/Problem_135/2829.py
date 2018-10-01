#!/usr/bin/python

import sys

def read_grid(f):
	result = []
	for x in xrange(4):
		result.append(f.readline().rstrip().split(' '))

	return result

def compare_grid(first, second):
	result = []

	for x in first:
		if x in second:
			result.append(x)

	if len(result) == 1:
		return result[0]

	elif len(result) == 0:
		return 'Volunteer cheated!'

	return 'Bad magician!'

input_file = open(sys.argv[1])

cases = int(input_file.readline())

for case in xrange(cases):
	print 'Case #'+str(case+1)+':',

	first_choice = int(input_file.readline())
	first_grid = read_grid(input_file)[first_choice-1]

	second_choice = int(input_file.readline())
	second_grid = read_grid(input_file)[second_choice-1]

	print compare_grid(first_grid, second_grid)

input_file.close()
