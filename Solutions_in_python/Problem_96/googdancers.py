f=open('test.txt','r')
q=open('ans.txt','w')

for i in range(1,1+int(f.readline())):
	arrr=[int(j) for j in f.readline().split()]
	s= arrr[1]
	p=arrr[2]
	nums=arrr[3:]
	wins,surprises=0,0
	for j in nums:
		if j>=3*p-2 and j>=p:
			wins+=1
		elif j>=3*p-4 and j>=p:
			surprises+=1
	print 'Case #' + str(i) + ': ' + str(wins+min(surprises,s))
	q.write('Case #' + str(i) + ': ' + str(wins+min(surprises,s)) + '\n')
q.close()
		
