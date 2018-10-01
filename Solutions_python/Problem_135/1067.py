import numpy as np
import sys

def parse_board(fh):
	T = int(next(fh))
	cases = []
	for _ in xrange(T):
		row1 = int(next(fh))
		cards1 = np.empty((4,4),dtype=int)
		for i in xrange(4):
			cards1[i] = map(int,next(fh).split())
		row2 = int(next(fh))
		cards2 = np.empty((4,4),dtype=int)
		for i in xrange(4):
			cards2[i] = map(int,next(fh).split())
		cases.append((row1,cards1,row2,cards2))
	return cases

def solve_case(r1,c1,r2,c2):
	s1 = c1[r1-1]
	s2 = c2[r2-1]
	common = np.intersect1d(s1,s2)
	if len(common) == 1:
		return common[0]
	if len(common) > 1:
		return "Bad magician!"
	return "Volunteer cheated!"

def main():
	cases = parse_board(sys.stdin)
	for i,case in enumerate(cases):
		print "Case #%d: %s" % (i+1, solve_case(*case))

if __name__ == '__main__':
	main()
