from math import pi

numruns=int(input())
for run in range(numruns):
	n,k=[int(i) for i in input().split()]
	pank = [[int(i) for i in input().split()] for j in range(n)]
	pank.sort(key = lambda x:-x[1]*x[0])
	# print(pank)
	big=0
	for i in range(n):
		area=pank[i][0]**2+2*pank[i][0]*pank[i][1]
		for j in range(k-1):
			area+=2*pank[j+int(j>=i)][0]*pank[j+int(j>=i)][1]
		big=max(big,area)
	print('Case #'+str(run+1)+': '+str(pi*big))