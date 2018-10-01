def flip(st):
	s=""
	for i in range(0,len(st)):
		if st[i]=='-':
			s+='+'
		else:
			s+='-'
	return s
cases=int(raw_input())
for c in range(1,cases+1):
	st,n=raw_input().split()
	n=int(n)
	arr='+'*(len(st))
	count=0
	for i in range(0,len(st)-(n-1)):
		if st[i]=='+':
			continue
		else:
			st=st[0:i]+flip(st[i:i+n])+st[i+n:]
			count+=1
	print "Case #"+str(c)+":",
	if st==arr:
		print count
	else:
		print "IMPOSSIBLE"	