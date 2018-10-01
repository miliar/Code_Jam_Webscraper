import sys
T = int(sys.stdin.readline())

for t in range(T):
	A, B = map(int, sys.stdin.readline().strip().split())
	a = int(A**.5)
	b = int(B**.5)+2
	count = 0
	for fs in range(a,b):
		s = str(fs)
		if s==s[::-1]:
			FS = fs*fs
			s = str(FS)
			if A<=FS<=B and s==s[::-1]:
				count += 1
	print("Case #%s: %s" % (str(t+1), str(count)))
