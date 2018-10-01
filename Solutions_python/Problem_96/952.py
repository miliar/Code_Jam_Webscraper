def abc():
	test=0
	test=input()
	j=0
	while j < test:
		j=j+1
		count=0
		scases=0
		nstr=raw_input()
		nlist2= nstr.split()
		nlist=[]
		#print nlist2
		for i in nlist2:
			nlist.append(int(i))
		#print nlist
		n=nlist[0]
		s=nlist[1]
		p=nlist[2]
		score=[]
		for i in range(0,n):
			score.append(nlist[3+i])
		for i in score:
			#print (i)
			avg=i/3
			if avg>=p:
				count=count+1
			elif i-p >=0:
				if (i-p)/2 == p-1:
					count=count+1
				elif (i-p)/2 == p-2:
					scases=scases+1
		#print count
		#print scases
		count=count+min(scases,s)
		nval="Case #"
		nval=nval+str(j)+": "
		nval=nval+str(count)
		print(nval)

abc()
		