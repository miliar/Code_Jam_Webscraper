#!/usr/bin/env python

# Tanner Grehawick
# Google Code Jam 2017 Qualification Round
# Problem 2: Tidy Numbers

from sys import stdin

def tidy(digits):
	istidy = False
	while not istidy:
		istidy = True
		for i in range(len(digits) - 1):		
			h = digits[i]				# high order digit
			l = digits[i + 1]			# next lower order digit
			if (l < h):
				digits[i] -= 1
				for j in range(i + 1, len(digits)):
					digits[j] = 9					
				istidy = False
	return digits

sample_count = int(stdin.readline().strip())

for s in xrange(sample_count):
	line = stdin.readline().strip()
	digits = [int(d) for d in line]
	digits = tidy(digits)
	print("Case #{}: {}".format(s + 1, long("".join(str(d) for d in digits))))