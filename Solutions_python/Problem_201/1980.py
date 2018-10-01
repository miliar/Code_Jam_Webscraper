def max_gap2(arr2):
	a2=0
	b2=0
	gap2=-1
	i2=0
	while i2<len(arr2)-1:
		if arr2[i2]==1:
			pos2=i2+1
			gp2=0
			while arr2[pos2]!=1:
				gp2+=1
				pos2+=1
			if gap2<gp2:
				gap2=gp2
				a2=i2
				b2=pos2
			i2=pos2
		else:
			i2+=1
	return(a2,b2)





t2=int(input())
N2=[]
K2=[]
while t2>0:
	li2=input().strip().split(' ')

	N2.append(int(li2[0]))
	K2.append(int(li2[1]))
	t2-=1
for i2 in range(len(N2)):
	slots2=[int(0)]*(N2[i2]+2)
	mini2=[int(-1)]*N2[i2]
	maxi2=[int(-1)]*N2[i2]
	slots2[N2[i2]+1]=1
	slots2[0]=1
	for q2 in range(K2[i2]):
		(ind12,ind22)=max_gap2(slots2)
		slots2[(ind12+ind22)//2]=1
	ls2=0
	rs2=0
	for q2 in range((ind12+ind22)//2-1,0,-1):
		if slots2[q2]==0:
			ls2+=1
		else:
			break
	for q2 in range((ind12+ind22)//2+1,len(slots2)):
		if slots2[q2]==0:
			rs2+=1
		else:
			break
	print("Case #"+str(i2+1)+": "+str(max(ls2,rs2)),str(min(ls2,rs2)))