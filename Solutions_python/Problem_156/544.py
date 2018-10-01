case=input()
for t in range(1,case+1):
	input()
	l=map(int,raw_input().split())	
	ans=max(l)
	for i in range(1,max(l)):
		ans=min(ans,sum(map(lambda x:(x-1)/i,l))+i)
	print "Case #%d: %d"%(t,ans)