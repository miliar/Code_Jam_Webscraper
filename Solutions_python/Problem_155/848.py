def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()

for _t in range(_T):
	print('Case #%i:'%(_t+1)),

	n, string = raw_input().split()
	n = int(n)

	shyness = []

	for i in xrange(n+1):
		shyness.append(int(string[i]))

	count = 0
	up = 0


	for i in xrange(n+1):

		miss = i-up
		if miss > 0:
			count += miss
			up += miss

		up += shyness[i]

	print count
