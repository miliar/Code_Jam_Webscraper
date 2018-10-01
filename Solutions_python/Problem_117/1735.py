from numpy import *
fin = open('B-small-attempt0.in','r')
fout = open('output.txt','w')
T = eval(fin.readline())
for i in range(T):
	w = 0
	v = 0
	outputno = False
	data = fin.readline()
	data = data.split()
	N = eval(data[0])
	M = eval(data[1])
	a = zeros((N,M))
	for j in range(N):
		data2 = fin.readline()
		data2 = data2.split()
		for t in range(M):
			a[j][t] = data2[t]
	for j in xrange(N):
		if (outputno == True):
			break
		for t in xrange(M):
			if (outputno == True):
				break
			if(a[j][t]==1):
				for k in xrange(N):
					if(a[k][t] == 1):
						w = w+1
				for q in xrange(M):
					if(a[j][q]==1):
						v = v+1
				if((w==N) or (v==M)):
					w = 0
					v = 0
					continue
				else:
					print >> fout, "Case #%d: NO"%(i+1)
					outputno = True
	if (outputno == False):
		print >> fout, "Case #%d: YES"%(i+1)
fin.close()
fout.close()