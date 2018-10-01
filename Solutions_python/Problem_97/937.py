def abc():
	test=0
	test=input()
	j=0
	while j < test:
		j=j+1
		
		nstr=raw_input()
		nlist2= nstr.split()
		n1=int(nlist2[0])
		n2=int(nlist2[1])
		tab=[]
		for k in range(n1,n2+1):
			ostr=str(k)
			nstr=ostr
			for l in range(0,len(ostr)-1):
				nstr=ostr[-1]+ostr[0:len(ostr)-1]
				ostr=nstr
				nnum=int(nstr)
				if nnum!=k and nnum<=n2 and nnum>=n1:
					ins=[k,nnum]
					if ins not in tab:
						tab.append(ins)
			#print(tab)			
		nval="Case #"
		nval=nval+str(j)+": "
		nval=nval+str(len(tab)/2)
		print(nval)
						
					
abc()
		