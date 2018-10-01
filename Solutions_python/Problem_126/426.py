t=int(raw_input())
for i in xrange(1,t+1):
	ip=raw_input().split()
	l,n=str(ip[0]),int(ip[1])
	length=len(l)
	add=0	
	j=0
	while j<length:	
		nval=0
		temp=j
		while nval<=n:
			if j>length-1:
				break
			if l[j]!='a' and l[j]!='e' and l[j]!='i' and l[j]!='u' and l[j]!='o':
				nval+=1
			else:
				nval=0
			if nval>=n:
				add+=(length-j)
				break
			j+=1
		j=temp+1
	print "Case #%d: %d"%(i,add)
