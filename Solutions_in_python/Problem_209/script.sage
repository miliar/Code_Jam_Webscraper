fin = file("A-small-attempt2.in","r")
fout = file("A-small-attempt2.out","w")
T = Integer(fin.readline())
for ct in range(T):
	line = fin.readline().split()
	[N,K] = [Integer(line[0]),Integer(line[1])]
	[R,H] = [[],[]]
	for i in range(N):
		line = fin.readline().split()
		R.append(Integer(line[0]))
		H.append(Integer(line[1]))
	C = []
	M = []
	for i in range(N):
		C.append(R[i]*2^20+H[i])
	C.sort(reverse=True)
	for i in range(N):
		R[i] = floor(C[i]/2^20)
		H[i] = C[i] % 2^20
		M.append(2*R[i]*H[i])
	best = 0
	for i in range(0,N-K+1):
		C = []
		for j in range(i+1,N):
			C.append(M[j])
		C.sort(reverse=True)
		v = R[i]*(R[i] + 2*H[i])
		for j in range(0,K-1):
			v = v+C[j]
		if(v > best):
			best = v
	area = (best*pi).n(128)
	str = "%.10lf" % area
	strin = "Case #"+ZZ(ct+1).str()+": "+str+"\n"
	fout.write(strin)
fin.close()
fout.close()
