#!/usr/bin/python

t=input()
for i in range(t):
	inp=raw_input()
	a=int(inp.split()[0])
	b=int(inp.split()[1])
	d={}
	main_a=a
	while a<b:
		str_a=str(a)
		l=len(str_a)
		while (l-1):
			str_a=str_a[-1]+str_a[:-1]
			new_a=int(str_a)
			n=min(a, new_a)
			m=max(a,new_a)
			k=len(str(n))
			ha=((10**k)*n)+m
			if n>=main_a and m<=b and n<m and (ha not in  d):
				d[ha]=1
			l-=1
		a+=1
	count=len(d)
	print "Case #"+str(i+1)+": "+str(count)
