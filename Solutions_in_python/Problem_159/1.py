f=open('A-large.in','r')
f1=open('out.txt','w')
casenum=int(f.readline().replace('\n',''))
for i in range(0,casenum):
	i=i+1
	times=int(f.readline().replace('\n',''))
	num=f.readline().split()
	res1=0
	res2=0
	max=0
	pre=0
	for j in num:
		if int(j)<pre:
			res1=res1+pre-int(j)
			if (pre-int(j))>max:
				max=pre-int(j)
		pre=int(j)
	for k in num:
		if times==1:
			pass
		else:
			if int(k)<max:
				res2=res2+int(k)
			else:
				res2=res2+max
		times=times-1
	f1.write('Case #'+str(i)+': '+str(res1)+' '+str(res2)+'\n')
f.close()
f1.close()