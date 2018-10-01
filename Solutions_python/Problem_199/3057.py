t=int(input())
arr1=[]
arr2=[]
o_loop=t
while t>0:
	s=input().split(' ')
	arr1.append(s[0])
	arr2.append(int(s[1]))
	t-=1
for i in range(o_loop):
	c=0
	i_check=list(arr1[i])
	
	while '-' in i_check:
		index=''.join(i_check).rindex('-')
		#print(li,j)
		fl=arr2[i]
		if index-(fl-1)>=0:
			for p in range(index,index-fl,-1):
				if i_check[p]=='+':
					i_check[p]='-'
				else:
					i_check[p]='+'
			c+=1
		else:
			c=-2
			break	
		#print(li[i])
	if c==-2:
		print("Case #"+str(i+1)+": "+"IMPOSSIBLE")
	else:
		print("Case #"+str(i+1)+": "+str(c))


			
		
