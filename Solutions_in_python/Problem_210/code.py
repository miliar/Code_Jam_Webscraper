t=int(input())
for ij in range(1,t+1):
	ac,aj=[int(s) for s in input().split(" ")]
	acti=[]
	for i in range(1,ac+aj+1):
		a,b=[int(s) for s in input().split(" ")]
		acti.append([a,b])
	if(ac*aj==0 and ac+aj==1):
		#if(acti[0]>=720 or acti[1]<=720):
			#print("Case #{}: {}".format(ij, 2 ))
		#else:
		print("Case #{}: {}".format(ij, 2 ))
	elif(ac*aj==0):
		a1=min(acti)
		a2=max(acti)
		tots=a1[1]-a1[0]+a2[1]-a2[0]
		#print(a1,a2)
		if(a1[0]>=720 or a2[1]<=720):
			print("Case #{}: {}".format(ij, 2 ))
		elif(a2[1]-a1[0]<=720):
			print("Case #{}: {}".format(ij, 2 ))
		elif(a1[1]+1440-a2[0]<=720):
			print("Case #{}: {}".format(ij, 2 ))
		else:
			print("Case #{}: {}".format(ij, 4 ))
	else:
		a1=min(acti)
		a2=max(acti)		
		if(a2[0]>=720 or a1[1]<=720):
			print("Case #{}: {}".format(ij, 2 ))
		else:
			print("Case #{}: {}".format(ij, 2 ))
			
				
	#print("Case #{}: {}".format(ij, 1 ))
