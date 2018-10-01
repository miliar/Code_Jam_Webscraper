import fractions as frac

f = open('2.in','r')
o = open('out.dat','w')

n = int(f.readline())

for i in xrange(n):
	A = f.readline().split()
	N = int(A[0])
	t = [int(A[j+1]) for j in xrange(N)]

	dt = [abs(t[j+1]-t[j]) for j in xrange(N-1)]
	
	gcd = dt[0]
	for j in xrange(1,N-1):
		gcd = frac.gcd(gcd,dt[j])
	
	a = t[0] % gcd
	if a:
		o.write('Case #' + str(i+1) + ': '+ str(gcd-a) +'\n')
	else:
		o.write('Case #' + str(i+1) + ': '+ str(a) +'\n')