#!/usr/bin/python

import sys

if len(sys.argv) <= 1:
	sys.exit(0)

f = file(sys.argv[1], 'r')
w = file(sys.argv[1] + '.out', 'w')

lines = f.readlines()
f.close()

controldata = lines[0].rstrip('\n').split(' ')
del lines[0]

def searching(phrase, term):
	#print "P: %30s, T: %20s" % (phrase, term)
	if len(term) == 0:
		return 1
	elif len(phrase) == 0:
		return 0
	else:
		result = phrase.find(term[0])
	#	print result
		if result >= 0:
			return searching(phrase[result+1:], term) + searching(phrase[result+1:], term[1:])
		else:
			return 0

case = 1
for line in lines:
	line = line.rstrip('\n')
	w.write("Case #%d: %04d\n" % (case, searching(line, "welcome to code jam") % 10000))
	case += 1

w.close()
