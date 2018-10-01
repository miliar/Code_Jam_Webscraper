def oversize(s,k):
	num=0
	while not all(s):
		final=s[::-1].index(0)
		if len(s)-final<k:
			return "IMPOSSIBLE"
		for i in range(k):
			s[~(final+i)]=1-s[~(final+i)]
		num+=1
	return num

f=open('A-large.in','r')
g=open('A-large.out','w')
for i in range(1,int(f.readline().strip())+1):
	s,k=f.readline().split()
	s,k=list(map(lambda x:'-+'.index(x),s)),int(k)
	print('Case #{}: {}'.format(i,oversize(s,k)),file=g)