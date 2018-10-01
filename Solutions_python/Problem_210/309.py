

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	for i in range(n):
		a=input()
		a=a.split()
		a1,a2=int(a[0]),int(a[1])
		l=[]
		for j in range(a1):
			b=input()
			b=b.split()
			l.append([int(b[0]),int(b[1]),0])
		for j in range(a2):
			b=input()
			b=b.split()
			l.append([int(b[0]),int(b[1]),1])
		inpute[i]=[a1,a2,l]
	return inpute

E=entre()

nb=0
for T in E:
	nb+=1
	r=0
	t=[0,0]
	tt=[0,0]
	tm=[[],[]]
	ttm=0
	T[2].sort()
	l=T[2]
	ab=True
	tt[l[0][2]]+=l[0][0]
	tt[l[len(l)-1][2]]+=1440-l[len(l)-1][1]
	for x in range(len(l)):
		t[l[x][2]]+=l[x][1]-l[x][0]
		if x<len(l)-1:
			if t[l[x][2]]==t[l[x+1][2]]:
				tt[l[x][2]]+=l[x+1][0]-l[x][1]
				tm[l[x][2]].append(l[x+1][0]-l[x][1])
			else:
				ttm+=l[x+1][0]-l[x][1]
				r+=1
	if l[0][2]!= l[len(l)-1][2]:
		r+=1
		ttm+=l[0][0]+1440-l[len(l)-1][1]
	else:
		tm[l[0][2]].append(l[0][0]+1440-l[len(l)-1][1])
	"""if t[0]+tt[0]+ttm<720 :
		tm[1].sort(reverse=True)
		ab=False
		if l[0][2]==1 and l[len(l)-1][2]==1:
			if l[0][0]>1440-l[len(l)-1][1]:
				r+=1
				ttm+=l[0][0]
				if t[0]+tt[0]+ttm<720 :
					r+=1
					ttm+=1440-l[len(l)-1][1]
			else:
				r+=1
				ttm+=1440-l[len(l)-1][1]
				if t[0]+tt[0]+ttm<720 :
					r+=1
					ttm+=l[0][0]
		elif l[0][2]==1 : 
			ttm+=l[0][0]
		elif l[len(l)-1][2]==1:
			ttm+=1440-l[len(l)-1][1]
		while t[0]+tt[0]+ttm<720 : 
			ttm+=tm[1].pop(0)
			r+=2
	if t[1]+tt[1]+ttm<720 and ab :
		tm[0].sort(reverse=True)
		if l[0][2]==0 and l[len(l)-1][2]==0:
			if l[0][0]>1440-l[len(l)-1][1]:
				r+=1
				ttm+=l[0][0]
				if t[1]+tt[1]+ttm<720 :
					r+=1
					ttm+=1440-l[len(l)-1][1]
			else:
				r+=1
				ttm+=1440-l[len(l)-1][1]
				if t[1]+tt[1]+ttm<720 :
					r+=1
					ttm+=l[0][0]
		elif l[0][2]==0 : 
			ttm+=l[0][0]
		elif l[len(l)-1][2]==0:
			ttm+=1440-l[len(l)-1][1]
		while t[1]+tt[1]+ttm<720 : 
			ttm+=tm[0].pop(0)
			r+=2"""
	tm[0].sort(reverse=True)
	tm[1].sort(reverse=True)
	while t[0]+tt[0]+ttm<720 : 
			r+=2
			ttm+=tm[1].pop(0)
	while t[1]+tt[1]+ttm<720 : 
			r+=2
			ttm+=tm[0].pop(0)
	print("Case #"+str(nb)+": "+str(r))
