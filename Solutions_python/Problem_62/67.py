
fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

T = int(fin.readline())
for test in range(0, T):
	N = int(fin.readline())
	ans = 0
	lines = []
	for _ in range(0, N):
		A, B = map(int, fin.readline().split())
		for a, b in lines:
			if (a>A and b<B) or (a<A and b>B):
				ans += 1
		lines.append((A, B))
	
	fout.write("Case #%d: %d\n" % (test+1, ans))
