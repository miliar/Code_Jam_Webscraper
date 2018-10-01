fin = open('AL.in', 'r')
fout = open('AL.out', 'w')

for i in range(int(fin.readline().strip())):
	tmp = fin.readline().strip().split(' ')
	smax = int(tmp[0])
	shy = [int(a) for a in tmp[1]]
	total = 0
	f = 0
	for j in range (smax+1):
		if j > 0:
			if shy[j] > 0 and j > total:
				f = f + (j - total)
				total = total + (j - total)
		total += shy[j]
	fout.write('Case #'+str(i+1)+': '+str(f)+'\n')
		
fout.close()
fin.close()