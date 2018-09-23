def getMaxMin(n, k):
	duples = [(n//2, (n-1)//2)]
	currIdx = 1
	if k == 1:
		return duples[0]
	lastIdx = 0
	while currIdx < k and len(duples)>0:
		lastIdx = currIdx
		newDuples = []
		for duple in duples:
			for x in duple:
				if x > 0:
					newDuples.append((x//2, (x-1)//2))
		duples = newDuples
		currIdx += len(duples)
	if len(duples) == 0:
		return (0,0)
	duples.sort(key = lambda x : (x[1], x[0]), reverse = True)
	return duples[k-lastIdx-1]

if __name__ == '__main__':
	T = int(input().strip())
	for i in range(T):
		n, k = map(int, input().strip().split(' '))
		M, m = getMaxMin(n, k)
		print('Case #{}: {} {}'.format(i+1, M, m))