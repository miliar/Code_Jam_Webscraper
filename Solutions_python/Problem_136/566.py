#!/usr/bin/env python

def main():
	fi = open('input.txt', 'r')

	total_T = int(fi.readline())

	for T in xrange(1,total_T+1):
		C,F,X = map(float, fi.readline().rstrip('\n').split())
		c=0.0
		f=2.0
		t=0.0
		# v = map(long, f.readline().rstrip('\n').split())

		# print E,R,N
		# print v
		# print C,F,X

		# print 

		print 'Case #{}: {}'.format(T, '%.7f' % next(t, f, C, F, X))

def next(t, f, C, F, X):
	while True:
		nt, nf = C/f+t, f+F

		if (nt + X/nf) < (X/f+t):
			t, f = nt, nf
		else:
			return X/f+t



	# nt, nf = C/f+t, f+F

	# if (nt + X/nf) < (X/f+t):
	# 	return next(nt, nf, C, F, X)
	# else:
	# 	return X/f+t



if __name__ == '__main__':
	main()