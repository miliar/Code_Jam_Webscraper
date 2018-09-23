import os
import sys

def solved(d):
	return sorted(d) == d

def result_from_digits(d):
	return int(''.join([str(x) for x in d]))

def get_tidy(digits, current):
	if len(digits) == 0:
		return current

	# not ordered
	if digits[-1] > current[0]:
		current = [9] * len(current)
		digits[-1] -= 1

	return get_tidy(digits[:-1], [digits[-1]] + current)

def solve_single(p):
	# p is str
	digits = [int(d) for d in str(p)]

	if len(digits) == 0:
		raise ValueError('wtf why no digits')

	elif len(digits) == 1:
		return p

	if solved(digits):
		return p

	return result_from_digits(get_tidy(digits[:-1], digits[-1:]))

def solve(in_file, out_file):
	lines = file(in_file, 'r').readlines()
	assert int(lines[0]) == len(lines) - 1

	solutions = [solve_single(*line.split()) for line in lines[1:]]
	solution_text = '\n'.join([('Case #%d: %s' % (i + 1, str(s))) for (i, s) in enumerate(solutions)])
	file(out_file, 'wb').write(solution_text)

def test_algo():
	assert solve_single(0) == 0
	assert solve_single(9) == 9
	assert solve_single(45) == 45
	assert solve_single(12345) == 12345
	assert solve_single(54) == 49
	assert solve_single(1000) == 999
	assert solve_single(11000) == 9999
	assert solve_single(132) == 129
	assert solve_single(7) == 7
	assert solve_single(111111111111111110) == 99999999999999999
	assert solve_single(12345677788889999) == 12345677788889999

def test_program():
	test_input = '''4
132
1000
7
111111111111111110'''
	test_output = '''Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999'''

	in_file_name = 'test_file.txt'
	out_file_name = 'result.txt'

	file(in_file_name, 'wb').write(test_input)
	solve(in_file_name, out_file_name)

	assert file(out_file_name, 'rb').read() == test_output

	os.unlink(in_file_name)
	os.unlink(out_file_name)

if __name__ == '__main__':
	solve(sys.argv[1], sys.argv[2])