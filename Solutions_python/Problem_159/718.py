T = int(raw_input())
cas = 0
f = open('out.txt', 'w')
while T > 0:
	T -= 1
	n = int(raw_input())
	data = map(int, raw_input().split())
	sum1 = 0
	sum2 = 0
	maxn = 0
	for i in xrange(1, n):
		if data[i] < data[i - 1]:
			sum1 += - data[i] + data[i - 1]
			maxn = max(data[i - 1] - data[i], maxn)
	for i in xrange(0, n - 1):
		sum2 += min(maxn, data[i]);
	cas += 1
	f.write('Case #' + str(cas) + ': ' + str(sum1) + ' ' + str(sum2) + '\n')
