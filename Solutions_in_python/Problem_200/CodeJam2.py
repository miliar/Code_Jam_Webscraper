T=int(raw_input())
a=0
e=[]
while a<T:
	b=raw_input()
	d=[]
	f=0
	while f<len(b):
		d.append(int(b[f]))
		f=f+1
	e.append(d)
	a=a+1

a=0
while a<T:
	g=0
	h=e[a]
	while g+1<len(h) and h[g]<=h[g+1]:
		 g=g+1

	if g<>len(h)-1:
		i=g+1
		while i<len(h):
			h[i]=9
			i=i+1
		while g>0 and h[g-1] == h[g]:
			h[g]=9
			g=g-1
		h[g]=h[g]-1

	k=0
	if h[0]==0:
		k=1
	j=""
	while k<len(h):
		j=j+str(h[k])
		k=k+1
			
	q=a+1
	r="Case #"+str(q)+": "+str(j)
	print r
	a=a+1





 