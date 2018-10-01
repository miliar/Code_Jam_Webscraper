import sys

T = int(raw_input())

for case in range(T):
	s = raw_input().split(' ')
	A = int(s[0])
	B = int(s[1])
	map = {}
	ctr = 0

	for i in range(A, B + 1):
		map[i] = []

	for i in range(A, B + 1):
		l = len(str(B))
		s = str(i).zfill(l)
		for j in range(1, len(s)):
			x = int(s[-j:] + s[0:l-j])
			if i < x and x >= A and x <= B and x != i and x not in map[i]:
				map[i].append(x)
				ctr = ctr + 1
	#print map
	sys.stdout.write("Case #" + str(case + 1) + ": " + str(ctr) + '\n')