import sys
import math

eps = 0.0001 # 1e-4

def run(N,K,U,P):
	assert N == K

	while U > 0:
		j = min(xrange(N), key = lambda k: P[k])
		if P[j] >= 1.0:
			assert P[j] == 1.0
			break

		P[j] += min(U,eps)
		U -= min(U,eps)

	ret = 1.0
	for p in P:
		ret *= p
	return ret

if __name__ == '__main__':
	T = int(raw_input())
	for t in xrange(T):
		(N,K) = map(int, raw_input().split())
		U = float(raw_input())
		P = map(float, raw_input().split())

		print "Case #%d: %.6f" % (t+1, run(N,K,U,P))
