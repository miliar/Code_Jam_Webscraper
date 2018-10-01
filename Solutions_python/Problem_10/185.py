import sys
fc = sys.argv[1]
inf = file('A-'+fc+'.in')
outf = file('A-'+fc+'.out','w')

for T in range(1,1+int(inf.readline().strip())):
	# P = Maximum per key
	# K = Keys available
	# L = Alphabet size
	(P,K,L) = map(int,inf.readline().strip().split(' '))
	F = map(int,inf.readline().strip().split(' '))
	F.sort(reverse=True)
	A = K # Keys left
	B = 1 # Position
	C = 0 # Total presses
	for x in F:
		C += B*x
		A = A - 1
		if A == 0: (A,B) = (K,B+1)

	print >> outf, 'Case #'+str(T)+': '+str(C)
		
print 'Great success.'
