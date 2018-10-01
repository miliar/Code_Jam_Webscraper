#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline())

for case in xrange(1, cases + 1):
	print "Case #%d:" % case,
	line = sys.stdin.readline().strip().split()
	combines = line[1:1 + int(line[0])]
	line = line[1 + int(line[0]):]
	opposes = line[1:1 + int(line[0])]
	invocation = line[-1]
	# key, final pair
	# value, replacement
	combine = {}
	for c in combines:
		combine[c[:2]] = c[-1]
		combine[c[-2::-1]] = c[-1]
	# key, letter to be added
	# value, letters that need to be checked
	oppose = {}
	for o in opposes:
		if o[0] not in oppose:
			oppose[o[0]] = set()
		if o[1] not in oppose:
			oppose[o[1]] = set()
		oppose[o[0]].add(o[1])
		oppose[o[1]].add(o[0])

	order_state = []
	count_state = {}
	for letter in invocation:
		while len(order_state) > 0:
			last = order_state.pop()
			count_state[last] -= 1
			final = last + letter
			if final in combine:
				letter = combine[final]
			else:
				order_state.append(last)
				count_state[last] += 1
				break
		clear = False
		if letter in oppose:
			for o in oppose[letter]:
				if o in count_state and count_state[o] > 0:
					clear = True
					break
		if clear:
			order_state = []
			count_state = {}
		else:
			order_state.append(letter)
			if letter not in count_state:
				count_state[letter] = 0
			count_state[letter] += 1
	ans = '['
	ans += ', '.join(order_state)
	ans += ']'
	print ans
