def signs(n,m,x,y,z,A):
	i = 0
	while i < n:
		yield A[i % m]
		A[i % m] = (x*A[i%m]+y*(i+1))%z
		i += 1

def solve(n,m,x,y,z,A):
	B = [1]*n
	S = list(signs(n,m,x,y,z,A))
	if n == 0:
		return 0
	if n == 1:
		return 1
	for l in range(n-2,-1,-1):
			for q in range(l+1, len(S)):
				if S[l] < S[q]:
					B[l] += B[q]
	return sum(B)

def solveFile(path):
	f = open(path)
	for i in range(1,int(f.readline())+1):
		l = f.readline().strip().split()
		A = []
		for q in range(0,int(l[1])):
			A.append(int(f.readline()))
		print "Case #%d: %d" % (i, solve(int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]),A) % 1000000007)