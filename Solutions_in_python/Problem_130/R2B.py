t=input()
for ii in range(t) :
	n,p=map(int,raw_input().split())
	l=[]
	tt=2**n
	for i in range(n) :
		if p<=2**(n-i-1) :
			l+='W'
		else :
			l+='L' 
			p=p-2**(n-i-1)

	print "Case #%d:"%(ii+1),

	f1=2
	for c in l :
		if c=='L' :
			f1=f1*2
		else :
			break
	f1=f1-2
	print min(2**n-1,f1),


	cnt=0
	for c in l :
		if c=='W' :
			cnt=cnt+1
	cnt2=0
	for c in l :
		cnt2=cnt2+1
		if c=='L' :
			break
	cnt=min(cnt,cnt2)

	print 2**n-2**cnt


			
		