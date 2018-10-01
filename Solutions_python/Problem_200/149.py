def untidy_index(N):
	digits = list(str(N))

	n = len(digits)
	for i in range(n-1):
		if digits[i] > digits[i+1]:
			return i
	return None

def is_tidy(N):
	i = untidy_index(N)
	if i is None:
		return True
	return False

def brute_tidy(N):
	if is_tidy(N):
		return N
	return brute_tidy(N-1)

def tidy(N):
	if is_tidy(N):
		return N

	i = untidy_index(N)

	digits = list(str(N))
	digits[i+1:] = ['0' for _ in digits[i+1:]]

	N2 = int(''.join(digits)) 

	return tidy(N2 - 1)

def load(f):
    lines = open(f).read().split('\n')
    n = int(lines[0])
    Ns = [int(s) for s in lines[1:] if s != '']
    assert n == len(Ns)
    return Ns

def run(f):
	output = solve(load(f))
	f2 = f + '.out'
	with open(f2, 'w') as fh:
		fh.write(output)
	print 'wrote output to', f2

def solve(Ns):
	output = []
	for i, N in enumerate(Ns):
		output += ['Case #%d: %d' % (i+1, tidy(N))]
	return '\n'.join(output) + '\n'


def test(up_to):
	for N in range(up_to):
		assert brute_tidy(N) == tidy(N)
	return 'passed'

example_input = [132, 1000, 7, 111111111111111110]

example_output = \
"""Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999
"""

assert solve(example_input) == example_output
