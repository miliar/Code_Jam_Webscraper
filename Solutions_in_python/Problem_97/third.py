import sys
input = open(sys.argv[1])
input.readline()
lines = 1
for line in input:
	A, B = line.strip().split()
	a = int(A)
	b = int(B)
	casecount = 0
	q = -1337
	for C in range(a, b + 1):
		n = str(C)
		for i in range(1,len(n)):
			m = int(n[i:] + n[:i])
			if a <= int(n) < m <= b:
				if m != q:
					'print(a,n,m,b)'
					casecount += 1
					q = m
	print('Case #' + str(lines) + ': ' + str(casecount))
	lines += 1
