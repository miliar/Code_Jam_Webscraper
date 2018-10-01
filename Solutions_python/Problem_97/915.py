import random
from collections import defaultdict

size = 2 * 1000 * 1000

fat = [0]
for i in xrange(1, size + 1): fat.append(i)
def find(x):
	r = (x if x == fat[x] else find(fat[x]))
	fat[x] = r
	return r
def merge(x, y):
	x = find(x)
	y = find(y)
	if random.randint(0, 1): fat[x] = y
	else: fat[y] = x

rem = [False] * (size + 5)

for x in xrange(1, size + 1):
	if not rem[x]:
		rem[x] = True
		y = x
		for i in xrange(len(str(x)) - 1):
			y = str(y)
			y = y[-1] + y[:-1]
			y = int(y)
			if len(str(y)) == len(str(x)) and y != x and y <= size:
				merge(x, y)
				rem[y] = True

T = int(raw_input())
for idx in xrange(T):
	A, B = map(int, raw_input().split())
	
	cnt = defaultdict(int)
	for x in xrange(A, B + 1):
		cnt[find(x)] += 1
	
	ans = 0
	for v in cnt.itervalues():
		ans += v * (v - 1)
	print 'Case #%d: %d' % (idx + 1, ans / 2)


