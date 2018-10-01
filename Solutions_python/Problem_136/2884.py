import lib
import numpy as np

@lib.wrapper
def solution(input, output):
	T = input.int()
	for case in xrange(1,T+1):
		C, F, X = input.float_tuple()
		n_max = max(int(X/C-2.0/F), 0)
		t = np.sum([C/(2.0+n*F) for n in range(n_max)]) + X/(2.+n_max*F)
		output.result(case, t)

if __name__ == '__main__':
	solution("B-large.in", "B-large.out")
