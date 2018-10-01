import sys

def permute(X):
	p = []
	if len(X) == 1: return [X]
	if not X: return []
	p.extend([[X[0]] + Y for Y in permute(X[1:])])
	p.extend([Y for Y in permute(X[1:])])
	return p

def pure(Li):
	if len(Li) == 1: return True
	i = len(Li) - 1 # 31
	while True:
		try:
			i = Li.index(i + 1) # 11
		except ValueError:
			return False
		if i == 0:
			return True
	return False

cached = """2 1
3 2
4 3
5 5
6 8
7 14
8 24
9 43
10 77
11 140
12 256
13 472
14 874
15 1628
16 3045
17 5719
18 10780
19 20388
20 38674
21 73562
22 140268
23 268066
24 513350
25 984911"""

if __name__=="__main__":
	cache = {}
	for line in cached.split("\n"):
		i, num = map(int, line.split())
		cache[i] = num % 100003
	f = open(sys.argv[1])
	cases = int(f.readline())
	for case in xrange(1, cases+1):
		N = int(f.readline())
		print "Case #%d: %d" % (case, cache[N])
