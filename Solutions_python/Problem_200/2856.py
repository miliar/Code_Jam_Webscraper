def fun(n,x,tr,ov):
	if x>=len(n): return [0]
	for i in range(9,-1,-1):
		if i>=tr and (i<=n[x] or (i>n[x] and ov)):
			#print(x,i,n[x])
			if i<n[x]: ov=True
			else: False
			tmp=fun(n,x+1,i,ov)
			if tmp!=False: return [i]+tmp
	return False
			
if __name__=='__main__':
	for t in range(int(input())):
		n=input()
		m=fun([int(i) for i in n],0,0,False)
		ans=''.join([str(i) for i in m[:-1] if i>0])
		print('Case #{0}: {1}'.format(t+1,ans))
