#!/usr/bin/python
a=raw_input()
ls=a.split(" ")
k=int(ls[0])
d=int(ls[1])
n=int(ls[2])
w=[]
for i in range(0,d):
	a=raw_input()
	w.append(a)
for i in range(0,n):
	a=raw_input()
	b=""
	s=[]
	c=0
	flag=0
	for j in range(0,len(a)):
		if(a[j]=='('):
			flag=1
		elif(a[j]==')'):
			flag=0
			s.append(b)
			b=""
			c=c+1
		elif(flag==0):
			b=b+a[j]
			s.append(b)
			c=c+1
			b=""
		else:
			b=b+a[j]
	#print s
	cnt=0
	for j in range(0,d):
		flag=0
		for m in range(0,k):
			if(s[m].find(w[j][m])==-1):
				flag=1
				break
		if(flag==0):
			cnt=cnt+1
	ss="Case #"+str(i+1)+": "+str(cnt)
	print ss

