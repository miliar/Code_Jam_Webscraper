tt = int(raw_input())
for nn in range(tt):
	x,w,r,t,n=map(float,raw_input().split())
	n=int(n)
	st=[]
	cnt=0
	for i in range(n):
		tmp=tuple(map(float,raw_input().split()))
		toput=(tmp[2],tmp[1]-tmp[0])
		st.append(toput)
		cnt+=toput[1]
	st.sort()
	time=t
	res=0.0
	trav=0
	cnt=x-cnt
###	print cnt
	if cnt/r>t:
		res=res+time
		res+=(cnt-t*r)/w
		time=0
	else:
		res=res+cnt/r
		time-=cnt/r
###	print time,'time',res
	
	for i in range(n):
###		print time
		if st[i][1]/(r+st[i][0])>time:
			res=res+time
			res=res+(st[i][1]-time*(r+st[i][0]))/(st[i][0]+w)
			time=0
		else:
			res=res+st[i][1]/(r+st[i][0])
			time-=st[i][1]/(r+st[i][0])
	print "Case #%d:"%(nn+1),res



	

