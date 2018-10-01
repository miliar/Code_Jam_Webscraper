#!/usr/bin/python2.7
# -*-coding:Utf-8 -*
f,s,i=open('A-small-attempt0.in','r'),open('sorti.txt','w'),1
n = int(f.readline())

if n>=1 and n<=100:
	while i<=n:
		val1 = int(f.readline())
		if val1 <1 or val1 > 4:
			break
		k=1
		while k<=4:
			if k == val1:
				ligne1 = (f.readline().rstrip('\n\r')).split(" ")
			else:
				f.readline()
			k+=1
		k=1
		val2 = int(f.readline())
		if val2 <1 or val2>4:
			break
		while k<=4:
			if k == val2:
				ligne2 = (f.readline().rstrip('\n\r')).split(" ")
			else:
				f.readline()
			k+=1

		cpt,elm = 0,0
		for el in ligne1:
			if el in ligne2:
				cpt,elm= cpt+1,int(el)
		if cpt == 0:
			var="Case #"+str(i)+": Volunteer cheated!\n"
		elif cpt == 1:
			var="Case #"+str(i)+": "+str(elm)+"\n"
		elif cpt:
			var="Case #"+str(i)+": Bad magician!\n"
		s.write(var)
		i+=1
