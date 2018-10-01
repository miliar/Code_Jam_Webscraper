#!/usr/bin/env python

FILE_NAME_BASE = 'B-small-attempt1'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	n, r, o, y, g, b, v = (int(x) for x in inp.readline().split())
	assert n == r + o + y + g + b + v
	return n, r, o, y, g, b, v

def solve(n, r, o, y, g, b, v):
	manes = [
			#BYR
		0,	#000
		r,	#001
		y,	#010
		o,	#011
		b,	#100
		v,	#101
		g,	#110
		0	#111
		]
	letters = '-RYOBVG-'

	searchOrder = sorted(xrange(1, 7), key=manes.__getitem__, reverse=True)
	stables = []
	while True:
		col1 = max(
			(col for col in searchOrder),
			key=manes.__getitem__
			)
		col2 = max(
			(col for col in searchOrder if col != col1),
			key=manes.__getitem__
			)
		if manes[col1] == 0:
			break
		stables.append(col1)
		manes[col1] -= 1
		if manes[col2] == 0:
			break
		stables.append(col2)
		manes[col2] -= 1

	if manes != [0] * 8 or stables[-1] == stables[0]:
		return 'IMPOSSIBLE'
	else:
		solution = ''.join(letters[color] for color in stables)
		assert len(solution) == n
		assert solution.count('R') == r
		assert solution.count('Y') == y
		assert solution.count('B') == b
		assert 'RR' not in solution + solution[0]
		assert 'YY' not in solution + solution[0]
		assert 'BB' not in solution + solution[0]
		return solution

def main():
	import sys
	sys.setrecursionlimit(RECURSION_LIMIT)

	import resource
	soft, hard = resource.getrlimit(resource.RLIMIT_AS)
	resource.setrlimit(resource.RLIMIT_AS, (MEM_LIMIT_GB * 1024 ** 3, hard))

	with open(FILE_NAME_BASE + '.in', 'r') as inp:
		numCases = int(inp.readline())
		inputs = [parse(inp) for _ in xrange(numCases)]

	if NUM_PROCESSES == 0:
		runners = [lambda inp=inp: apply(solve, inp) for inp in inputs]
	else:
		from multiprocessing import Pool
		from signal import SIGINT, SIG_IGN, signal
		pool = Pool(NUM_PROCESSES, signal, (SIGINT, SIG_IGN))
		runners = [pool.apply_async(solve, inp).get for inp in inputs]
		pool.close()

	caseFmt = '%' + str(len(str(numCases))) + 'd'
	progressFmt = '[%s/%s] %%s\n' % (caseFmt, caseFmt)
	with open(FILE_NAME_BASE + '.out', 'w') as out:
		for case, runner in enumerate(runners, 1):
			result = runner()
			out.write('Case #%d: %s\n' % (case, result))
			out.flush()
			sys.stderr.write(progressFmt % (case, numCases, result))

if __name__ == '__main__':
	main()
