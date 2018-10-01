#~ Bot Trust
file=open('A-large.in','r')
TC=int(file.readline()[:-1])
#~ TC=1
for case in range(TC):
	c=file.readline()[:-1]
	#~ c='10 O 58 B 34 O 58 B 10 O 91 B 69 O 47 O 84 B 98 B 5'
	c=c.split()
	N=int(c[0])
	#~ print(N)
	def merge(x):
		l=list()
		for i in range(0,len(x),2):
			l.append(x[i]+x[i+1])
		return l
	act=merge(c[1:])
	ol,bl=list(),list()
	for a in act:
		if(a[0]=='O'):	ol.append(a)
		else:			bl.append(a)
	ol.reverse()
	bl.reverse()
	act.reverse()
	#~ print(act,ol,bl)
	#~ print('Time\tOrange\t\t\tBlue')
	O_status,B_status=1,1
	seconds=0
	go=N
	oact,bact='O1','B1'
	if(ol):	oact=ol.pop()
	if(bl):	bact=bl.pop()
	if(act):	d=act.pop()
	while (go):
		if(d[0]=='O'):
			cycle=int(d[1:])-O_status
			if(cycle<0):	cycle=-1*cycle
			#~ print(d,O_status,cycle)
			for e in range(cycle+1):
				seconds+=1
				#~ print(seconds,end='\t')
				if(int(d[1:]) > O_status):
					O_status+=1
					#~ print('Move to %d,%d'%(O_status,int(d[1:])),end='\t\t')
				elif(int(d[1:]) < O_status):
					O_status-=1
					#~ print('Move to %d,%d'%(O_status,int(d[1:])),end='\t\t')
				elif(int(d[1:]) == O_status):
					#~ print('Push button %d,%d'%(O_status,int(d[1:])),end='\t\t')
					if(act):
						go-=1
						if(ol):	oact=ol.pop()
						d=act.pop()
					else:	go=0
				#	*	*	*
				if(int(bact[1:]) > B_status):
					B_status+=1
					#~ print('Move to %d,%d'%(B_status,int(bact[1:])),end='\t\t')
				elif(int(bact[1:]) < B_status):
					B_status-=1
					#~ print('Move to %d,%d'%(B_status,int(bact[1:])),end='\t\t')
				elif(int(bact[1:]) == B_status):
					B_status=B_status
					#~ print('stay at %d,%d'%(B_status,int(bact[1:])),end='\t\t')
				#~ print([oact,bact,d,ol,bl,act])
		elif(d[0]=='B'):
			cycle=int(d[1:])-B_status
			if(cycle<0):	cycle=-1*cycle
			#~ print(d,B_status)
			for e in range(cycle+1):
				seconds+=1
				#~ print(seconds,end='\t')
				if(int(oact[1:]) > O_status):
					O_status+=1
					#~ print('Move to %d,%d'%(O_status,int(oact[1:])),end='\t\t')
				elif(int(oact[1:]) < O_status):
					O_status-=1
					#~ print('Move to %d,%d'%(B_status,int(oact[1:])),end='\t\t')
				elif(int(oact[1:]) == O_status):
					O_status=O_status
					#~ print('stay at %d,%d'%(O_status,int(oact[1:])),end='\t\t')
				#	*	*	*
				if(int(d[1:]) > B_status):
					B_status+=1
					#~ print('Move to %d,%d'%(B_status,int(d[1:])),end='\t\t')
				elif(int(d[1:]) < B_status):
					B_status-=1
					#~ print('Move to %d,%d'%(B_status,int(d[1:])),end='\t\t')
				elif(int(d[1:]) == B_status):
					#~ print('Push button %d,%d'%(B_status,int(d[1:])),end='\t\t')
					if(act):
							go-=1
							if(bl):	bact=bl.pop()
							d=act.pop()
					else:	go=0
				#~ print([oact,bact,d,ol,bl,act])
		#~ print('go',go,d)
	print('Case #%d: %d'%(case+1,seconds))
file.close()