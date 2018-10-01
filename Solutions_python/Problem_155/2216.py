fin = open("F:\projects\codejam\A-small-practice.in","r")
T = int(fin.readline())
fout = open("F:\projects\codejam\A-small-practice.out","w")
for i in range(T):
	line = fin.readline()
	splits = line.split(' ')
	sm = int(splits[0])
	np = []
	acc = []
	res = 0
	for j in range(sm+1):
		np.append(int(splits[1][j]))
		acc.append(0)
		if (j==0):
			acc[j]=0
		else:
			acc[j] = np[j-1]+acc[j-1]
		while (j>0 and acc[j]<j):
			res = res +1
			np[j-1] = np[j-1]+1
			acc[j] = np[j-1]+acc[j-1]
#			print acc
#	print np
	out =  "Case #%d: %d\n"%(i+1,res)
	fout.write(out)