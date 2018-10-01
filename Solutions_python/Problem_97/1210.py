f=open("teste","r")
pika=f.read()
pika=pika.split()
t=int(pika.pop(0))
o=0
while t!=0:
	o=o+1
	p=0
	l=0
	a=int(pika.pop(0))
	b=int(pika.pop(0))
	g=[]
	for i in range(a,b+1):
		print i,
		g=g+[i]
	while len(g)>1:
		s=list(str(g[0]))
		g.pop(0)
		aw=g[0]
		ow=[]
		for j in range(len(s)-1):
			s=s+[s.pop(0)]
			k="".join(s)
			k=int(k)
                        if s[0]==0:
                                csa=0
			elif k in g and (k in ow)==False:
				p=p+1
				print k,
				#print aw,k,ow,p
				ow=ow+[k]
		l=l+1
        q=open("respgoo.txt","a")
        q.write("Case #"+str(o)+": "+str(p)+"\n")
	t=t-1
