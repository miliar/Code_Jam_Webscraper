t = int(input())
def dc(x, y):
	if y==1:
		if x%2==0:
			return x//2,(x-1)//2
		else:
			return x//2,x//2
	if y%2:
		x = (x-1)//2
	else:
		x //= 2
	y //= 2
	return dc(x,y)

for c in range(1,t+1):
	a,b = map(int,input().split())
	mx,mn = dc(a,b)
	print("Case #{}: {} {}".format(c,mx,mn))
	
