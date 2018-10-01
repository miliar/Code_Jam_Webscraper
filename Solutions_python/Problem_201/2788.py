import bisect
t= input()
i=0
def ls_rs(now):
	h=now/2
	if now%2==0:
		
		ls=h-1
		rs=h
	else:
		ls=h
		rs=h
	op=[]
	if rs<ls:
		op=[ls]
		op.append(rs)
	else:
		op=[rs]
		op.append(ls)
	return op
ls_rs_dict={}
ls_rs_dict[0]=[0,0]
while i<t:
	n_k= raw_input()
	n=int (n_k.split(" ")[0])
	k=int(n_k.split(" ")[1])
	i=i+1
	
	empty = [0]*n

	s=0
	l=n-1
	ls=[n-1]*n
	rs=[n-1]*n
	p=0
	while p<n:
		ls[p]=p
		rs[p]=n-1-p
		p=p+1
	j=0
	if n%2==0:
		half=n/2-1
	else:
		half=n/2
	bfs=[]
	now1=n
	
 	while j<k:
 		op=[]
 		if now1 not in ls_rs_dict:
 			ls_rs_dict[now1]=ls_rs(now1)
 		op=ls_rs_dict[now1]
 		#print ls_rs_dict[now1]
 		for el in ls_rs_dict[now1]:
 			#bisect.insort(bfs, el)
 			#print bfs
			bfs.append(el)
		#print bfs 
		now1=max(bfs)
		bfs.remove(now1)
		
		#print now1
		j=j+1
	# print ls_rs_dict[0]
	print "Case #%d: %d %d"%(i,op[0],op[1])
	
		

		


		
