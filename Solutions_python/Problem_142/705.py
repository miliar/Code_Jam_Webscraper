import itertools
import os.path
import sys
import math
import collections

def process(ifile, ofile):
	test_case_count = int(ifile.readline())
	for test_case_num in range(1, test_case_count + 1):
		N = int(ifile.readline())
		ss = [ifile.readline().strip() for _ in range(N)]
		rhs = solve(N, ss)
		ofile.write('Case #{}: {}\n'.format(test_case_num, rhs))
		print 'Case #{}/{}: {}'.format(test_case_num, test_case_count, rhs)
		print

def cost(vec, n):
	return sum(abs(v - n) for v in vec)

def solve(N, ss):
	prev = ' '
	ltrs = []
	for ch in ss[0]:
		if ch == prev:
			continue
		ltrs.append(ch)
		prev = ch

	work = [[] for _ in range(len(ltrs))]
	for i, s in enumerate(ss):
		prev = ' '
		idx = -1
		for ch in s:
			if ch == prev:
				work[idx][-1] += 1
			else:
				idx += 1
				if idx >= len(ltrs):
					return 'Fegla won'
				if ch != ltrs[idx]:
					return 'Fegla won'
				work[idx].append(1)
				prev = ch

	print repr(work)
	if not all(len(w) == len(ss) for w in work):
		return 'Fegla won'

	total = 0
	for stage in work:
		avg = sum(stage) / len(stage)
		low = int(math.floor(avg))
		high = int(math.ceil(avg))
		total += min(cost(stage, low), cost(stage, high))
			
	return total
	

def main():
	if len(sys.argv) < 2:
		print 'Usage: {} ex|small|large [num]'.format(os.path.basename(sys.argv[0]))
		sys.exit(1)
	size = sys.argv[1]
	num = sys.argv[2] if len(sys.argv) >= 3 else '0'
	assert size in ('ex', 'small', 'large')
	cyclename = 'A-' + size
	if size != 'ex':
		cyclename += '-{}'.format(num)
	with open('source\\{}.in'.format(cyclename), 'rb') as i:
		with open('source\\{}.out'.format(cyclename), 'wb') as o:
			process(i, o)
		

if __name__ == '__main__':
	main()
