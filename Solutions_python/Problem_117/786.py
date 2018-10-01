import sys
import math
if __name__ == "__main__":
	T = int(sys.stdin.readline().strip())
	for caseno in xrange(T):
		N,M = map(int, sys.stdin.readline().strip().split(' '))
		a = []
		for i in xrange(1,N+1):
			a.append(map(int, sys.stdin.readline().strip().split(' ')))

		Break = False
		for i in xrange(N):
			for j in xrange(M):
				hor = True
				vert = True
				for k in xrange (N):
					if a[i][j] < a[k][j]:
						hor = False
				for l in xrange (M):
					if a[i][j] < a[i][l]:
						vert = False
						
				if hor == False and vert == False:
					#print "i:" , i, " j:", j, " k:", k, " l:", l
					Break = True
					break
			if (Break):
				break
		if (not Break):
			result = "YES"
		else:
			result = "NO"
		print "Case #%d: %s" % (caseno + 1, result)
