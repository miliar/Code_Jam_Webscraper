f=open("C-small-1-attempt1.in")
for _ in xrange(int(f.readline().strip())):
	n,k=map(int,f.readline().strip().split())
	s=list("0"+"_"*n+"0")
	i,a,b=0,0,0
	while i<k:
		temp,r=[],0
		for x in xrange(len(s)):
			if s[x]=="0":temp.append(x)
		for y in xrange(len(temp)-1):
			if temp[y+1]-temp[y]>r:
				a,b=temp[y+1],temp[y]
				r=a-b
		s[b+r/2]="0"
		i+=1
	print "Case #%d: %d %d"%(_+1,max(r/2,a-b-r/2)-1,min(r/2,a-b-r/2)-1)