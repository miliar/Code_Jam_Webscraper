n=int(input())

for tc in range(0,n):
	n-=1

	x=[0 for i in range(0,20)] 

	a=raw_input()
	
	for i in range (0,len(a)):
			if(a[i]=='w'):
				x[0]+=1
			elif(a[i]=='e'):
				x[1]+=x[0]
				x[6]+=x[5]
				x[14]+=x[13]
			elif(a[i]=='l'):
				x[2]+=x[1]
			elif(a[i]=='c'):
				x[3]+=x[2]
				x[11]+=x[10]
			elif(a[i]=='o'):
				x[4]+=x[3]
				x[9]+=x[8]
				x[12]+=x[11]
			elif(a[i]=='m'):
				x[5]+=x[4]
				x[18]+=x[17]
			elif(a[i]==' '):
				x[7]+=x[6]
				x[10]+=x[9]
				x[15]+=x[14]
			elif(a[i]=='t'):
				x[8]+=x[7]
			elif(a[i]=='d'):
				x[13]+=x[12]
			elif(a[i]=='j'):
				x[16]+=x[15]
			elif(a[i]=='a'):
				x[17]+=x[16]

	ans = "Case #"+str(tc+1)+": "
	leng=len(str(x[18]%10000))
	for tt in range(leng,4):
		ans+="0"
	ans+=str(x[18]%10000)
	print ans
