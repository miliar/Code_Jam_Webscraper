#!/usr/bin/env python

numTests = int(raw_input())

for testNo in xrange(1, numTests + 1):
	rowNo = int(raw_input())
	row = (int(j) for j in [raw_input() for i in xrange(4)][rowNo - 1].split())
	rowNo = int(raw_input())
	row2 = (int(j) for j in [raw_input() for i in xrange(4)][rowNo - 1].split())

	answer = set(row).intersection(set(row2))
	print 'Case #{0}:'.format(testNo),
	if len(answer) == 0:
		print 'Volunteer cheated!'
	elif len(answer) == 1:
		print answer.pop()
	else:
		print 'Bad magician!'
