#normal: ti >= 3p-2
#suprising: ti >= 3p-4 (and <= 3p-2) (p > 1)

def testCase():
	line = [int(token) for token in raw_input().split()]
	N = line[0]
	S = line[1]
	p = line[2]
	t = line[3:]
	assert len(t) == N

	result = 0
	result_S = 0
	for ti in t:
		if ti >= 3 * p - 2:
			result += 1
		elif ti >= p and ti >= 3 * p - 4:
			result_S += 1
	return result + min(result_S, S)

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %d" % (i+1, testCase())
