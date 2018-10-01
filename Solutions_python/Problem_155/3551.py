t=int(raw_input())
for i in xrange(1,t+1):
	a,s=raw_input().split()
	a=int(a)
	n=0
	ans=0
	for j in xrange(a+1):
		x=int(s[j])
		if x!=0:
			if j<=n :
				n=n+x
			else:
				ans=ans+j-n
				n=n+x+ans
		#print ans,n
	st="Case #"+repr(i)+": "+repr(ans)
	print st
	
		