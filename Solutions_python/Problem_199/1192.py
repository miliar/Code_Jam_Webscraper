T=int(raw_input())
a=0
e=[]
while a<T:
	b=[x for x in raw_input().split()]
	c=b[0]
	d=[]
	f=0
	while f<len(c):
		if c[f]=="+":
			d.append(1)
		if c[f]=="-":
			d.append(0)
		f=f+1
	e.append([d,int(b[1])])
	a=a+1

a=0
while a<T:
	g=0
	h=e[a]
	i=h[0]
	l=h[1]
	j=0
	while g<len(i)-l+1:
		if i[g]==0:
			j=j+1
			k=0
			while k<l:
				i[g+k]=1-i[g+k]
				k=k+1
		g=g+1
	p=1
	g=1
	while g<l:
		if i[len(i)-l+g]==0:
			p=0
		g=g+1
	if p==1: 
		q=a+1
		r="Case #"+str(q)+": "+str(j)
		print r
	else: 
		q=a+1
		r="Case #"+str(q)+": IMPOSSIBLE"
		print r

	a=a+1





 