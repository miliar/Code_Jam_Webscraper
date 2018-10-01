#!/usr/bin/python

def tidy(x):
	temp1=9
	while (x/10)!=0:
		temp2=x%10
		#print temp1,temp2
		if temp2>temp1:
			return 0
		temp1=temp2
		x=(x/10)
	if x>temp2:
		return 0
	else:
		return 1

#print tidy(307)

	
f=open("B-large.in",'r')
T=int(f.readline())
N=[]
for line in f:
	N.append(int(line))

f.close()

g=open("output B-large.txt","w")

for i in range(T):
	p=1
		
	n=N[i]
	output="Case #"+str(i+1)+":"
	if n/10==0:
		print >>g, output,n
	else:
		while n>0:
			if tidy(n)==1:
				print "Answer = ", n
				break
			else:
				x=(10**p)
				y=x-1
				z=(10**(p-1))
				if (n%x)==y:
					p+=1
					z=(10**(p-1))
					n-=z
					#print n
				else:
					n-=z
					#print n
		print >>g, output,n

g.close()

