
fr=open('A-large.in','r')
fw=open('out_large.txt','w')
T=int(fr.readline())
for z in range(T):
	s,k = fr.readline().split(' ')
	s,k,l=list(s),int(k),len(s)
	ans=0
	for i in range(l):
		if l-i>=k and s[i]=='-':
			ans+=1
			for j in range(k): 
				s[i+j]='+' if s[i+j]=='-' else '-'
	p=str(ans)
	for i in range(k):
		if l-1>=i and s[l-1-i]=='-':
			p='IMPOSSIBLE'
			break
	fw.write('Case #%d: %s\n'%(z+1,p))
#with open('out.txt','w') as w:
#		for i in a: w.write('%s'%i)