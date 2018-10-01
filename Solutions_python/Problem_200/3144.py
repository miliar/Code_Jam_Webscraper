T=int(raw_input())+1

for i in range (1,T):
	nbr=list(raw_input())
	l=len(nbr)-1
	ll=len(nbr)

	if l==0:
		print 'Case #%d: %c'%(i,''.join(nbr))
	else:
		for j in range (l,0,-1):
			if nbr[j]<nbr[j-1]:
				for k in range (j,ll):
					nbr[k]='9'
				nbr[j-1]=str(int(nbr[j-1])-1)

		print 'Case #%d: %d'%(i,int(''.join(nbr)))

	
	
