t1=int(input())
arr=[]
while t1>0:
		n2=int(input())
		arr.append(n2)
		t1-=1
for p in range(len(arr)):
	flg=0
	if arr[p]<10:
		num=arr[p]
	else:
		#if arr[p]%10!=0:
		m3=arr[p]
		while flg!=1:
			
			l=str(m3)
			li=list(str(m3))
			eq=-1
			for i in range(len(li)-1):
				if int(li[i])>int(li[i+1]):
					ind=i
					flg=0
					break
				else:
					flg=1
				
			if flg==0:
				strng=''
				for k in range(i):
					strng=strng+str(li[k])
				no=int(li[i])-1
				strng=strng+str(no)
				
				for k in range(len(strng),len(li)):
					strng=strng+'9'
				num=int(strng)
				m3=num
			else:
				num=m3
		
	strng="Case #"+str((p+1))+": "+str(num)
	print(strng)
			

