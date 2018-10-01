t=int(raw_input())
for i in range(0, t):
	s, a=raw_input().strip().split()
	s=int(s)
	a=[int(e) for e in a]
	ans=0
	cur=0
	for j in range(0, s+1):
		if cur>=j:
			cur+=a[j]
		else:
			ans+=(j-cur)
			cur+=(a[j]+j-cur)
	print "Case #"+str(i+1)+": "+str(ans)
		