inf=open('A-large.in','r')
outf=open('large1.out','w')
count_case=int(inf.readline())
count=1
for line in inf:
	data=line.split()
	c1=int(data[1][0])
	tmp=[c1]
	for i in range(1,int(data[0])+1):
		tmp.append(c1-i)
		c1+=int(data[1][i])
	result=min(tmp)
	if result<0:
		result=-result
	else:
		result=0
	outf.write("Case #"+str(count)+": "+str(result)+'\n')
	count+=1
inf.close()
outf.close()


