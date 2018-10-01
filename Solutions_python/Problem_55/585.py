r=open('C-small.in','r')
w=open('C-small.out','w')
T=int(r.readline())
for i in range(0,T): # Each day
	S=0; s=0; 
	a=r.readline(); a=a.split(' '); R=int(a[0]); K=int(a[1]); N=int(a[2])
	Q=r.readline(); Q=Q.split(' ')
	for a in range(0,R): # Each ride 
		s=0
		for b in range(0,N): # Each group
			x=int(Q[0]); 
			if (s+x<=K):
				s+=x
				del Q[0]; Q.append(x)
			else:
				break
		S+=s
	w.write('Case #{0}: {1}\n'.format(i+1,S))
r.close();w.close()