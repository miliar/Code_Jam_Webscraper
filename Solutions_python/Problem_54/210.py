#!/usr/bin/env python

FILE_NAME_BASE = 'B-large'
NUM_PROCESSES = 4

def parse(inp):
	numbers = [int(x) for x in inp.readline().split()]
	length = numbers[0]
	assert length == len(numbers) - 1
	return numbers[1 : ],

def gcd(a, b):
	'''Returns the greatest common divisor of a and b.
	'''
	while a != 0:
		a, b = b % a, a
	return b

def solve(events):
	events = sorted(events)
	intervals = [
		events[i + 1] - events[i]
		for i in xrange(len(events) - 1)
		]
	divider = reduce(gcd, intervals, 0)
	phase = events[0] % divider
	#print divider, phase, events
	return 0 if phase == 0 else divider - phase

if __name__ == '__main__':
	from multiprocessing import Pool
	pool = Pool(NUM_PROCESSES)
	inp = open(FILE_NAME_BASE + '.in', 'r')
	numCases = int(inp.readline())
	results = [
		pool.apply_async(solve, parse(inp))
		for _ in range(numCases)
		]
	inp.close()
	out = open(FILE_NAME_BASE + '.out', 'w')
	for case, result in enumerate(results):
		out.write('Case #%d: %s\n' % (case + 1, result.get()))
		out.flush()
	out.close()
