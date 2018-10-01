import sys
from math import pi
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")
for t in range(int(input())) : 
	n,k = map(int,input().split())
	ls = []
	for i in range(n) : 
		r,h = map(int,input().split())
		ls.append([r,h])
	ls = sorted(ls , key = lambda x:x[0],reverse = True)
	mans = 0
	#print(ls)
	for i in range(n) : 
		#print(ls)
		ans = ls[i][0]**2 + 2*ls[i][0]*ls[i][1]
		b = sorted(ls[i+1:],key = lambda x:x[0]*x[1],reverse = True)
		#print(b)
		if len(b) < (k-1) : 
			break
		j = 1
		for x in b :
			if j >= k : break
			ans += 2*x[0]*x[1]
			j += 1
		#print(ans)
		mans = max(mans,ans)
	print('Case #',t+1,': ',pi*mans,sep = '')
		
		
		