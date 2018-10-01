import os
import sys

def parse_pan(s):
	return [(1 if x == '+' else 0) for x in s]

def print_pan(p):
	print ''.join([('+' if x else '-') for x in p])

def solved(p):
	return all(p)

def flip(p, pos, k):
	for i in xrange(pos, pos + k):
		p[i] ^= 1

def get_flips(p, k):
	moves = 0
	while True:
		#print_pan(p)

		if solved(p):
			return moves
		
		pos = p.index(0)

		if len(p) < pos + k:
			return None

		flip(p, pos, k)
		moves += 1

def solve_pan(s, k):
	return get_flips(parse_pan(s), int(k))

def solve(in_file, out_file):
	lines = file(in_file, 'r').readlines()
	assert int(lines[0]) == len(lines) - 1

	solutions = [solve_pan(*line.split()) for line in lines[1:]]
	solution_text = '\n'.join([('Case #%d: %s' % (i + 1, 'IMPOSSIBLE' if s is None else str(s))) for (i, s) in enumerate(solutions)])
	file(out_file, 'wb').write(solution_text)

def test_algo():
	assert solve_pan('---+-++-', 3) == 3
	assert solve_pan('+++++', 4) == 0
	assert solve_pan('-+-+-', 4) is None

def test_program():
	test_input = '''3
---+-++- 3
+++++ 4
-+-+- 4'''
	test_output = '''Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE'''

	in_file_name = 'test_file.txt'
	out_file_name = 'result.txt'

	file(in_file_name, 'wb').write(test_input)
	solve(in_file_name, out_file_name)

	assert file(out_file_name, 'rb').read() == test_output

	os.unlink(in_file_name)
	os.unlink(out_file_name)

if __name__ == '__main__':
	solve(sys.argv[1], sys.argv[2])