import sys

fin = open(sys.argv[1], "r")
fout = open("A.out", "w")

T = int(fin.readline())
for tt in xrange(T):
	N = int(fin.readline())
	m = map(int,fin.readline().split())
#	print m
	out1 = 0
	out2 = 0
	maxdif = 0
	for i in range(1,N):
		if m[i]<m[i-1]:
			out1 += m[i-1] - m[i]
			maxdif = max(maxdif, m[i-1] - m[i]) 	
#	print maxdif
	for i in range(N-1):
		if m[i]<maxdif:
			out2 += m[i]
		else:
			out2 +=maxdif	
#		print out2	


	fout.write("Case #" + str(tt+1) + ": " + str(out1) + " " + str(out2) + "\n")   