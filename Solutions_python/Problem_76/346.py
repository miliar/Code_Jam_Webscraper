#!/usr/bin/python

import sys

def do_case(case, line_data):
	y = 0
	for d in line_data:
		y ^= d

	if y != 0:
		print "Case #%d: NO" % case
	else:
		print "Case #%d: %d" % (case, sum(line_data, -line_data[0]))

data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

case = 1
while len(data_lines):
	data_lines.pop()
	line_data = data_lines.pop().split(' ')
	ds = sorted([long(x) for x in line_data])
	do_case(case, ds)
	case += 1
#	break
