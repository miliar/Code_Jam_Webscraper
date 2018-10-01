__author__ = 'donlnz'

import numpy as np

def read_problem(filename, callback, n_lines_case):
	with open(filename) as file:
		n_cases = int(file.readline())
		for i in range(n_cases):
			case = []
			for j in range(n_lines_case):
				case.append(file.readline()[:-1].split(' '))
			yield(callback(case))

def problem_1_callback(case):
	ans1 = int(case[0][0]) - 1
	rows1 = np.array(case[1:5], dtype=int)
	ans2 = int(case[5][0]) - 1
	rows2 = np.array(case[6:], dtype=int)

	candidates = filter(lambda x: x in rows2[ans2], rows1[ans1])
	candidates = [i for i in candidates]

	if len(candidates) == 1:
		return candidates[0]
	if len(candidates) > 1:
		return 'Bad magician!'
	return 'Volunteer cheated!'

case_n = 1
with open('../output/p1.txt', 'w') as file:
	for i in read_problem('../input/p1.in', problem_1_callback, 10):
		file.write('Case #{}: {}\n'.format(case_n, i))
		case_n += 1
