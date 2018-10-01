from math import factorial
m=0
def nodes(subs,words):
	c=set()
	for i in xrange(m):
		if subs&(1<<i):
			for j in xrange(len(words[i])+1):
				c.add(words[i][:j])
	#print "with ",subs,"get",[i for i in c]
	return len(c)
fin=open('D-small-attempt2.in')
fout=open('D.out','w')
cases=int(fin.readline())
def comp(els):
	els.sort()
	return tuple(els)
def check(a,b,c,els):
	if(a==c):
		b.add(comp(els))
		return a,b
	elif(c>a):
		b=set()
		b.add(comp(els))
		return c,b
	else:
		return a,b
for cas in xrange(1,cases+1):
	fout.write("Case #{}:".format(cas))
	m,n=map(int,fin.readline().split())
	s=[fin.readline().strip() for i in xrange(m)]
	best=0
	count=set()
	alls=(1<<m)
	if(n==1):
		best=nodes(alls-1,s)
		count=set()
		count.add(1)
	else:
		for i in xrange(1,alls-1):
			j=(alls-1)^i
			if(n==2):
				best,count=check(best,count,nodes(i,s)+nodes(j,s),[i,j])
			else:
				for k in xrange(1,alls-1):
					if(n==3):
						k=(i&k)
						i2=(i^k)
						if(k==0 or i==0):
							continue
						else:
							best,count=check(best,count,nodes(i2,s)+nodes(j,s)+nodes(k,s),[i2,j,k])
					elif(n==4):
						l=(k&j)
						j2=(j^l)
						k=(i&k)
						i2=(i^k)
						#if(cas==2): print i,j,k,l
						if(i==0 or k==0 or j==0 or l ==0):
							continue
						else:
							best,count=check(best,count,nodes(i2,s)+nodes(j2,s)+nodes(k,s)+nodes(l,s),[i2,j2,k,l])
	fout.write(" "+str(best)+" "+str(len(count)*factorial(n)))
	fout.write('\n')
fout.close()
fin.close()
	
