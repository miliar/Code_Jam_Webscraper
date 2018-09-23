def prints(id, val):
	print ("Case #",id,": ",val, sep='')



def solve (id):
	t= input().split()
	s= t[0]
	k= int(t[1])
	n= len(s)
	arr= []
	for i in range(0, n):
		if (s[i]=='+'):
			arr.append(1)
		else:
			arr.append(0)	
	res= 0 

	for i in range(0, n):
		if (arr[i]==0):
			if (i+k-1>=n):
				prints(id, "IMPOSSIBLE")
				return
			res=res+1
			for j in range(i, i+k):
				if (arr[j]==1):
					arr[j]= 0
				else:
					arr[j]= 1
	prints(id, res)					




t= int(input())
for i in range(1, t+1):
	solve(i) 		 