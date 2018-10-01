def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def solve(m, rate):
	n = 0
	for i in xrange(len(m)-1):
		if m[i] - 10*rate > m[i+1]:
			return -1
		n += 10*rate if m[i] >= 10*rate else m[i]

_T = readint()

for _t in range(_T):
	print('Case #%i:'%(_t+1)),

	N = readint()
	m = readarray(int)

	rate = 0
	res1 = 0
	for i in xrange(N-1):
		if m[i] > m[i+1]:
			rate = max(rate, (m[i]-m[i+1])/10.)
			res1 += m[i]-m[i+1]

	res2 = 0
	for i in xrange(N-1):
		 res2 += min(m[i], 10*rate)

	print res1, int(res2)


