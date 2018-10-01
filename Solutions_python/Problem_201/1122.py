dir="/home/yuxh/Desktop/c/c"



def divide(n):
	if n%2==0:
		return n//2,n//2
	else:
		return (n+1)//2,n//2

def magic(n,k):
	dic={n:1}
	for i in range(k-1):	
		m=max(dic)
		dic[m]-=1
		if dic[m]==0:
			del dic[m]
		a,b=divide(m-1)
		if a in dic:
			dic[a]+=1
		else:
			dic[a]=1
		if b in dic:
			dic[b]+=1
		else:
			dic[b]=1
	m=max(dic)
	return divide(m-1)
	
file=open(dir)
T=int(file.readline()[:-1])
for i in range(T):
	[a,b]=file.readline()[:-1].split()
	a=int(a)
	b=int(b)
	c,d=magic(a,b)
	print("Case #"+str(i+1)+": "+str(c)+" "+str(d))
