import lib
import numpy as np
from sets import Set

@lib.wrapper
def solution(input, output):
	T = input.int()
	for case in xrange(1,T+1):
		A, B, K = input.int_tuple()
		As = np.arange(A)
		Bs = np.arange(B)
		pairs = np.sum(np.bitwise_and(As,Bs[:,np.newaxis])<K)		
		output.result(case, pairs)

if __name__ == '__main__':
	solution("B-small-attempt0.in", "B-small-attempt0.out")
