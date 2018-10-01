T=int(raw_input())+1

for i in range (1,T):
	inp=raw_input()
	panck=list(inp.split(' ')[0])
	flip=int(inp.split(' ')[1])

	l=len(panck)-flip
	ll=len(panck)

	count=0
	
	for j in range (0,l+1):
		if panck[j]=='-':
			count+=1
			for k in range (j,j+flip):
				if(panck[k]=='+') :
					panck[k]='-'
				else:
					panck[k]='+'
			
	for j in range (l,ll):
		if panck[j]=='-' :
			print 'Case #%d: IMPOSSIBLE'%i
			count=-1
			break
	
	if count>-1 :
		print 'Case #%d: %d'%(i,count)

	
	
