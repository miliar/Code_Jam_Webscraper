import scipy.special as sps
from math import ceil

def mintime(C, F, X):
	optK = max(ceil(X/C - 2.0/F - 1.0), 0)
	return C*(sps.digamma(optK + 2.0/F) - sps.digamma(2.0/F))/F + X/(F*optK + 2.0)


def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [map(float, x.strip().split()) for x in fin.readlines()]
	fin.close()
	
	fout = open(out_name, 'w')
	fout.writelines(['Case #' + str(i) + ': ' + str(mintime(L[i][0], L[i][1], L[i][2])) + '\n' for i in xrange(1, len(L))])
	fout.close()
	
	return
	
#solve('B-small-attempt0.in', 'B-small-attempt0.out')
solve('B-large.in', 'B-large.out')

#solve('B-test.in', 'B-test.out')
