fin=open('A-large.in')
fout=open('A.out','w')
cases=int(fin.readline())
for cas in xrange(1,cases+1):
	fout.write("Case #{}:".format(cas))
	n,x=map(int,fin.readline().split())
	si=map(int,fin.readline().split())
	si.sort()
	a,b=0,n-1
	cost=0
	while(a<=b):
		#print a,b,si[a],si[b],cost
		if(a!=b and si[a]+si[b]<=x):
			cost+=1
			a+=1
			b-=1
		elif a!=b:
			cost+=1
			b-=1
		else:
			cost+=1
			b-=1
	fout.write(' '+str(cost))

	fout.write('\n')
fout.close()
fin.close()
	
