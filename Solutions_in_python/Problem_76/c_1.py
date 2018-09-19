import sys
def case():
	a = int(sys.stdin.readline()[:-1])
	b = sys.stdin.readline()[:-1]
	true_sum = 0
	xor_sum = 0
	min_candy = 1000001
	for c in b.split(' '):
		candy = int(c)
		if candy < min_candy:
			min_candy = candy
		true_sum += candy
		xor_sum = xor_sum ^ candy
	if xor_sum == 0:
		return true_sum - min_candy
	else:
		return -1

t = int(sys.stdin.readline()[:-1])
for i in range(t):
	r = case()
	if r == -1:
		print 'Case #{0}: NO'.format(i+1)
	else:
		print 'Case #{0}: {1}'.format(i+1, r)

