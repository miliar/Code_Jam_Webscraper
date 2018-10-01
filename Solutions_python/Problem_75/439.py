# python 3
T=int(input())
for t in range(1,T+1):
	args=[x for x in input().split()]
	#print(args)
	C=int(args[0])
	comb=dict()
	for i in range(1,C+1):
		comb[args[i][:2]]=args[i][2]
		comb[args[i][1]+args[i][0]]=args[i][2]
	#print(comb)
	D=int(args[C+1])
	opos=set()
	for i in range(C+2,C+D+2):
		opos.add(args[i])
		opos.add(args[i][1]+args[i][0])
	#print (opos)
	invok=args.pop()
	res=list()
	for c in invok:
		suite=False
		if len(res)==0:           
			res.append(c)
			continue
		if (res[-1]+c) in comb: 
			res[-1]=comb[res[-1]+c]
			continue
		for c2 in res:
			if (c+c2) in opos:
				res=[]
				suite=True
				break
		if suite: continue
		res.append(c)	
	ress='['
	for c in res:
		ress=ress+c+', '
	if len(res):ress=ress[:-2]+']'
	else: ress=ress+']'
	print("Case #"+str(t)+":",ress)