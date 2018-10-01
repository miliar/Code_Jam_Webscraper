t = int(raw_input())

def doOneBinary(leng, num):
	(lengMin, lengMax) = (leng - leng / 2 - 1, leng / 2)
	(numMin, numMax) = ((num - 1) / 2, (num - 1) - (num - 1) / 2)
	if numMin == numMax:
		return lengMin, numMin, leng
	else: 
		return lengMax, numMax, leng

def doAll(n, m):
	while m > 0:
		n, m, p = doOneBinary(n, m)
	return p

for i in xrange(1, t + 1):
	n, m = [int(x) for x in raw_input().split()]
	p = doAll(n, m)
	print "Case #{}: {} {}".format(i, p / 2, p - p / 2 - 1)