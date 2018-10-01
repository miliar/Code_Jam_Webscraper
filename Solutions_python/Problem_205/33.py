# Train Script
from collections import deque 

T=input()
for zz in range(T):
	Hd, Ad, Hk, Ak, B, D = [int(i) for i in raw_input().split(' ')]
	st = set()
	st.add(str(Hd)+'*'+str(Ad)+'*'+str(Hk)+'*'+str(Ak))
	Q=deque()
	Q.append([Hd,Ad,Hk,Ak,0])
	ans=-1
	while len(Q):
		z=Q.popleft()
		if z[0]<=0: continue
		if z[2]<=0:
			ans=z[4]
			break
		mv=z[0]-z[3] if z[2]>z[1] else z[0]
		kp=str(mv)+'*'+str(z[1])+'*'+str(z[2]-z[1])+'*'+str(z[3])
		if kp not in st: 
			Q.append([mv,z[1],z[2]-z[1],z[3],z[4]+1])
			st.add(kp)
		
		kp=str(z[0]-z[3])+'*'+str(z[1]+B)+'*'+str(z[2])+'*'+str(z[3])
		if kp not in st: 
			Q.append([z[0]-z[3],z[1]+B,z[2],z[3],z[4]+1])
			st.add(kp)
		
		kp=str(Hd-z[3])+'*'+str(z[1])+'*'+str(z[2])+'*'+str(z[3])
		if kp not in st: 
			Q.append([Hd-z[3],z[1],z[2],z[3],z[4]+1])
			st.add(kp)
		
		mv = z[3]-D if z[3]>D else 0
		kp=str(z[0]-mv)+'*'+str(z[1])+'*'+str(z[2])+'*'+str(mv)
		if kp not in st: 
			Q.append([z[0]-mv,z[1],z[2],mv,z[4]+1])
			st.add(kp)
	print 'Case #%d: %s'%(zz+1, str(ans) if ans>-1 else 'IMPOSSIBLE')