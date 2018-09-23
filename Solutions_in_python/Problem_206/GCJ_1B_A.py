T=int(input())
for roop1 in range(T):
	temp=input().split()
	D=int(temp[0])
	N=int(temp[1])
	ansTime=0
	for i in range(N):
		KS=[int(i) for i in input().split()]
		#print(KS)
		road=D-KS[0]
		#print(road/KS[1])
		if road/KS[1]>ansTime:
			ansTime=road/KS[1]
	ansSpead=D/ansTime
	
	
	print("Case #"+str(roop1+1)+": "+str(ansSpead))