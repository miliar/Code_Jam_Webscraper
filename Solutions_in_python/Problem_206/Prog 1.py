import math

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	for i in range(n):
		a=input()
		a=a.split()
		a1,a2=int(a[0]),int(a[1])
		s=[[0,0] for j in range(a2)]
		for  j in range(a2):
			b=input()
			b=b.split()
			b1,b2=int(b[0]),int(b[1])
			s[j][0],s[j][1]=b1,b2
		inpute[i]=[s,a1,a2]
	return inpute


nb=0
E=entre()
for T in E:
	nb+=1
	r=9999999999.0
	nch=T[2]
	ob=T[1]
	chs=T[0]
	for c in chs:
		if c[0]<ob :
			v=ob/((ob-c[0])/(c[1]*1.0))
			if r>v or r==9999999999.0:
				r=v
	if r==9999999999.0:
		r=(ob*1.0)
	print("Case #"+str(nb)+": %.6f"%r)
