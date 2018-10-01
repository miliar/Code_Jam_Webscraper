
def read_input(filename):
	f = open(filename)
	T = int(f.readline())

	test_cases = [None] * T

	for i in range(T):
		test_cases[i] = [float(x) for x in f.readline().split()]

	return test_cases

def solve_case(test_case):
	(C, F, X) = test_case

	Q = 2.0

	cur_min_time = X / Q
	cur_invest_time = 0

	n = 0

	while cur_invest_time < cur_min_time:
		cur_invest_time += C / (Q + n * F)
		run_time = X / (Q + (n+1)*F)

		total_time = cur_invest_time + run_time

		if total_time < cur_min_time:
			cur_min_time = total_time

		n += 1

	return cur_min_time

def solve(testid):
	inputfile = testid + '.in'
	outputfile = testid + '.out'

	test_cases = read_input(inputfile)

	results = [None] * len(test_cases)

	for i in range(len(test_cases)):
		results[i] = solve_case(test_cases[i])

	write_output(outputfile, results)

def write_output(outputfile, results):
	g = open(outputfile, 'w')
	t = 1
	for result in results:
		g.write('Case #{}: {:.7f}\n'.format(t, result))
		t += 1
	g.close()

if __name__ == '__main__':
#	solve('sample')
#	solve('B-small-attempt0')
	solve('B-large')



