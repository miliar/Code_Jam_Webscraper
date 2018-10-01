
def price(k):
	return k*N - k*(k-1)/2

def solve(N, lst):
	org = 0
	E = N*[0]
	O = N*[0]
	new = 0
	for (e,o,p) in lst:
		E[e] += p
		O[o] += p
		org += p*price(o - e)
	for k in range(0,N):
		for e in range(0,N - k):
			t = min(E[e],O[e+k])
			if t > 0:
				E[e] -= t
				O[e+k] -= t
				new += t*price(k)
	return org - new

T = int(raw_input())
for i in range(1, T+1):
	lst = [int(r) for r in raw_input().split(" ")]
	N = lst[0]
	M = lst[1]
	lst = [(0,0,0)]*M
	for j in range(0,M):
		tmp = [int(r) for r in raw_input().split(" ")]
		lst[j] = (tmp[0] - 1, tmp[1] - 1, tmp[2])
	print "Case #{0}: {1}".format(i, solve(N,lst))
