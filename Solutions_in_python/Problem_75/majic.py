#!/usr/bin/python

import sys

def do_case(case, steps):
	combine = {}
	oppose = []

	cc = long(steps.pop())
	while cc:
		s = steps.pop()
		combine[s[0:2]] = s[2:]
		combine[s[1:2]+s[0:1]] = s[2:]
		cc -= 1

	oc = long(steps.pop())
	while oc:
		s = steps.pop()
		oppose.append(set(s))
		oc -= 1

	steps.pop()
	invoke = steps.pop()

	elements = []
	for i in range(len(invoke)):
		elements.append( invoke[i:i+1] )
		combined = False
		clear = False
		l = len(elements)
		if l >= 2:
			s = ''.join(elements[l-2:l])
			if s in combine:
				elements[l-2:l] = combine[s]
				combined = True

		if not combined:
			elem_set = set(elements)
			for o in oppose:
				if o.issubset(elem_set):
					clear = True
					break

		if clear:
			elements = []

	print "Case #%d: [%s]" % (case, ', '.join(elements))


data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

case = 1
while len(data_lines):
#	print data_lines[len(data_lines)-1]
	line_data = data_lines.pop().split(' ')
	line_data.reverse()
	do_case(case, line_data)
	case += 1
#	break
