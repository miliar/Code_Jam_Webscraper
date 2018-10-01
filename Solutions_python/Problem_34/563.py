#!/usr/bin/python
st = raw_input()
st=st.split()

l=int(st[0])
d=int(st[1])
n=int(st[2])

dict = []
case = []
for i in range(d):
	dict.append(raw_input())
dict.sort()
for i in range(n):
	case.append(raw_input())

ind = 0
for t in case:
	ind = ind+1
	word = [ [] for qq in range(l) ]
	i=0
	while len(t)>0:
		char=t[0]
		if char=='(':
			t=t[1:]
			char=t[0]
			while char!=')':
				word[i].append(char)
				t=t[1:]
				char=t[0]
			i=i+1
			t=t[1:]
		else:
			word[i].append(char)
			i=i+1
			t=t[1:]

	n = 0
	for d in dict:
		ld = list(d)
		ok = 1
		for cdi in range(len(ld)):
			if word[cdi].count(ld[cdi])==0:
				ok=0
				break
		if ok:
			n = n+1

	print "Case #"+str(ind)+":",n

