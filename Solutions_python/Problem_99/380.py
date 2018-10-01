import sys

f = open(sys.argv[1],"r")

N = int(f.readline())

for c in range(N):
	(A,B) = map(int, f.readline().split())
	p = map(float, f.readline().split())
	expected = []
	for k in range(A+1):
		p_success = reduce(lambda m,n:m*n, p[:A-k] if p[:A-k] else [1])
		expected.append((B-A+2*k+1)*p_success + (2*k+2*B-A+2)*(1-p_success))
	expected.append(B+2)
	print "Case #" + str(c+1) + ": " + str(min(expected))
