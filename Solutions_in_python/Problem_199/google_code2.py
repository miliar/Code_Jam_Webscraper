t=int(raw_input())
for k in range(t):
	s=raw_input()
	ind=s.index(' ')
	n=int(s[ind+1:])
	s=list(s[:ind])	
	count=0
	for i in range(len(s)-n+1):
		if s[i]=='-':
			count+=1
			p=i
			for j in range(n):
				if s[p]=='-': s[p]='+'
				else: 
					s[p]='-'
				p+=1
	if '-' in s[len(s)-n:]: print "Case #%d: IMPOSSIBLE" % (k+1)
	else: print "Case #%d: %d" % (k+1,count)

