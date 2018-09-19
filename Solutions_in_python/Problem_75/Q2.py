#!/usr/bin/env python

import sys

def main():
	with open(sys.argv[1]) as f:
		lines = f.readlines()

		for i in range(1, len(lines)):
			result = solve(lines[i])
			print_result(i, result)

def print_result(case, result):
	result = '[' + ', '.join(result) + ']'
	print "Case #%d: %s" % (case, result)

def solve(line):
	parts = line.split()
	p = 0

	C = int(parts[p])
	Cs = parts[p+1:p+C+1]
	p += C + 1

	D = int(parts[p])
	Ds = parts[p+1:p+D+1]
	p += D + 1

	N = int(parts[p])
	Ns = parts[p+1]

	cmap = {}
	for char in 'QWERASDF':
		cmap[char] = {'c': {}, 'o': []}

	for c in Cs:
		cmap[c[0]]['c'][c[1]] = c[2]
		cmap[c[1]]['c'][c[0]] = c[2]

	for d in Ds:
		cmap[d[0]]['o'].append(d[1])
		cmap[d[1]]['o'].append(d[0])

	stack = []

	for char in Ns:
		stack.append(char)

		if len(stack) > 1:
			if cmap[char]['c'].has_key(stack[-2]):
				comb = cmap[char]['c'][stack[-2]]
				stack[-2:] = [comb]
			else:
				for opp in cmap[char]['o']:
					if opp in stack:
						stack = []
						break

	return stack

if __name__ == '__main__':
	main()
