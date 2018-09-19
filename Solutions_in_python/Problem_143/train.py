fich,sor,k=open('lio.in','r'),open('sorB1.txt','w'),1
T = int(fich.readline())
if T>=1 and T<=100:
	while k<=T:
		tab1=(fich.readline().rstrip('\n\r')).split(" ")
		A,B,K,cpt=int(tab1[0]),int(tab1[1]),int(tab1[2]),0
		for i in range(0,A):
			for j in range(0,B):
				if (i&j) < K:
					cpt+=1
		sor.write("Case #"+str(k)+": "+str(cpt)+"\n")
		k+=1

