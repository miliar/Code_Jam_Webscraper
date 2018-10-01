from math import sqrt
def pal(n): return str(n) == str(n)[::-1]
c=int(input())

def f(low,high):
	sql=int(sqrt(low))
	if sql**2<low:sql+=1
	t=0
	while sql**2<=high:
		if pal(sql) and pal(sql**2): t+=1
		sql+=1
	return str(t)
for i in range(c):
	l=input().split()
	print ("Case #"+str(i+1)+": "+f( int(l[0]) , int(l[1]) ))