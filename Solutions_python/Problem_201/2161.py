from itertools import islice
from collections import Counter
def parse_lines(lines) :
	return map(lambda s : problem_parse_line(s.strip()), 
		islice(lines, 1, None))

def format_solution(case, solution) :
	return f'Case #{case}: {solution}'

def problem_parse_line(line) :
	return tuple(map(int, line.split()))

def solve(n, k) :
	queue = Counter([n])
	mx = n
	last = None
	for _ in range(k) :
		queue.update([mx//2, max((mx-1)//2, 0)])
		last = [mx//2, max((mx-1)//2, 0)]
		queue[mx] -= 1
		if queue[mx] == 0 :
			queue.pop(mx)
			mx = max(queue)
	fst_min = min(queue) ; queue[fst_min] -= 1
	if queue[fst_min] == 0 :
		queue.pop(fst_min)
	return ' '.join(map(str, last))

print()

sol_file = open('solved2.txt', 'w')
with open('C-small-2-attempt0.in') as lines :
	for case, args in enumerate(parse_lines(lines), start=1) :
		print(format_solution(case, solve(*args)), file=sol_file)