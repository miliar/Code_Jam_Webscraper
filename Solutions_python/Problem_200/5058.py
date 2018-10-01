num1=int(input())
list1=[None]*num1
for i in range(0,num1+1):
	list1[i]=int(input())
	list2=[None]*list1[i]
	m=0
	for j in range(list1[i],0,-1):
		s=str(j)
		if(len(s)==1):
			list2[m]=s
			m=m+1;
		for k in range(0,len(s)-1):
			if(s[k]>s[k+1]):
				break;
			if(k==len(s)-2):
				list2[m]=s
				m=m+1;
	print("Case #"+str(i+1)+": "+list2[0])