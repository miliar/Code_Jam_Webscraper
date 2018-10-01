t=int(raw_input())
for ca in range(1,t+1):
	temp=raw_input()
	Na = [float(i) for i in temp.split()]
	c,f,x=Na
	coin=2
	totalT=0
	while True:
		t1=totalT+x/coin
		t2=totalT+(c/coin)
		if (t1>(t2	+(x/(coin+f)))):
			totalT=t2
			coin=coin+f
		else:
			totalT=t1
			break
	#print totalT
	print "Case #%i: %f" %(ca,totalT)











