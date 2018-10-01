# your code goes here
t=int(input())
for i in range(t):
	r=int(input())
	
	for j in range(r,0,-1):
		#print(j)
		s=str(j)
		if len(s)==1:
			print("Case #{0}: {1}".format(i+1,j))
			#print("len is 1")
			break
		l=len(s)
		flag=0
		for k in range(0,l-1):
			#print("both value {0} {1}".format(s[k],s[k+1]))
			if int(s[k])>int(s[k+1]):
				flag=1
				#print("comparing")
				break
		if flag==0:
			print("Case #{0}: {1}".format(i+1,j))
			#print("final ")
			break
		
