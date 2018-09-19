#~ Candy Splitting
#~Combination FORMULA	:	 n!/(r! * (n-r)!)
from math import factorial
file=open('C-small-attempt1.in','r')
TC=int(file.readline()[:-1])
Ncache=list()
Lcache=list()
for case in range(TC):
	n=int(file.readline()[:-1])
	#~ n=5
	xc=file.readline()[:-1]
	#~ xc='3 6 5'
	xc=xc.split()
	maxS=0
	def CLIST(k):
		L=list()
		FT=list()
		N=len(k)
		R=len(k)
		def RECUR(L,R):
			#~ print(L,r)
			if(R>0):
				#~ print('xx')
				if(not L):
					for i in range(N):
						RECUR([i],R-1)
				else:
					for i in range(N):
						if(i not in L):
							RECUR(L+[i],R-1)
			else:	
				FT.append(L)
		RECUR(L,R)
		RT=list()
		for j in FT:
			g=list()
			for o in j:
				g.append(k[o])
			RT.append(g)
		return (RT)
	def recur(l,r):
		#~ print(l,r)
		if(r>0):
			#~ print('xx')
			if(not l):
				for i in range(n):
					recur([i],r-1)
			else:
				for i in range(n):
					if(i not in l):
						recur(l+[i],r-1)
		else:	
			ln=0
			clist=CLIST(l)
			#~ print(clist)
			for lx in clist:
				if(lx not in ft):
					#~ print(l,lx in ft)
					ln+=1
			if(ln==len(clist)):
				ft.append(l)
			#~ print(ft)
	def tot(l):
		t=0
		for i in l:
			t=t.__xor__(i)
		return t
	def Otot(l):
		t=0
		for i in l:
			t+=i
		return t
	def original(l):
		r=list()
		for i in l:
			r.append(int(xc[i]))
		return r
	for i in range(1,int(n/2)+1):
		com=int((factorial(n)/factorial(n-i))/factorial(i))
		#~ print('i=%d,%d\tc=%d'%(i,(n-i),com))
		r=i
		ft=list()
		l=list()
		if(n in Ncache):
			ft=Lcache[Ncache.index(n)]
		else:
			Ncache.append(n)
			recur(l,r)
			Lcache.append(ft)
		for c in ft:
			nc=list()
			for i in range(n):
				if(i not in c):	nc.append(i)
			C,NC=original(c),original(nc)
			Patrick=tot(C)
			Sean=tot(NC)
			#~ print('p=',C,Patrick,'s=',NC,Sean)
			stot=Otot(NC)
			if(Patrick==Sean) and (stot > maxS):	maxS=stot
	if(maxS == 0):	maxS='NO'
	print('Case #%d:'%(case+1),maxS)