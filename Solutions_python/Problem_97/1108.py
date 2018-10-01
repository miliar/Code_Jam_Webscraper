def split(n):
	b=[]
	while(not(n==0)):
		a=n%10
		n=n/10
		b.append(a)
	return b
		
def join(n):
	n.reverse()
	s=0
	i=0
	for e in n:
		s=e*(10**i)+s
		i+=1		
	return s	
		
f1=open('C-small-attempt0.in','r')
f2=open('recycle.out','w')


k=f1.readline()
k.rstrip('\n')
t=1
while t<=int(k):
	s=f1.readline()
	s=s.rstrip('\n')
	s=s.split(' ')
	a=int(s[0])
	b=int(s[1])
	c=0
	j=[]
	

	for x in range(a,(b+1)):
		y=split(x)
		y.reverse()
	#	print 'in for 1'
		w=join(y)
		y.reverse()
		for z in range(len(str(x)),1,-1):
	#		print 'in for 2'
	#		print 'old y is :'+str(y)
	#		print 'z is'+str(z)
	#		print 'w is'+str(w)
			p=y.pop()
	#		print 'p is'+str(p)
			y.insert(0,p)
	#		print 'new y is'+str(y)
			q=join(y)
			y.reverse()
	#		print 'q is '+str(q)
			if(q>w and q<=b and q>=a):
	#			print 'in if'
				j1=[w,q]
				if j1 not in j:
					j.append(j1)
					c+=1
		
	
	temp='Case #'+str(t)+': '+str(c)+'\n'
	f2.write(temp)
	t+=1	
					
			
		
