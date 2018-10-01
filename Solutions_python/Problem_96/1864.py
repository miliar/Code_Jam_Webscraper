import string

def isS(a):
	return max(a)-min(a)==2

triplets={}
tripletss={}
for i in range(31):
	triplets[i]=[]
	tripletss[i]=set()

for i in range(11):
	for j in range(11):
		for k in range(11):
			if max((i,j,k))-min((i,j,k))<=2:
				tup=sorted((i,j,k))
				if str(tup) not in tripletss[i+j+k]:
					triplets[i+j+k].append(tup)
					tripletss[i+j+k].add(str(tup))

f=open('B-small-out.txt','w')
T=int(raw_input())
for t in range(1,T+1):
	d=map(int,string.split(raw_input(),' '))
	n=d[0]
	s=d[1]
	p=d[2]
	a=d[3:]

	m=0
	if n==1:
		for i in triplets[a[0]]:
			ss=0
			if isS(i):
				ss+=1
			if s==ss and max(i)>=p:
				m=1
	elif n==2:
		for i in triplets[a[0]]:
			for j in triplets[a[1]]:
				ss=0
				if isS(i):
					ss+=1
				if isS(j):
					ss+=1
				if s==ss:
					if max(i)>=p or max(j)>=p:
						m=1
					if max(i)>=p and max(j)>=p:
						m=2
	elif n==3:
		for i in triplets[a[0]]:
			for j in triplets[a[1]]:
				for k in triplets[a[2]]:
					ss=0
					if isS(i):
						ss+=1
					if isS(j):
						ss+=1
					if isS(k):
						ss+=1
					if s==ss:
						kk=0
						for ii in (i,j,k):
							if max(ii)>=p:
								kk+=1
						m=max(m,kk)

	f.write("Case #"+str(t)+": "+str(m)+"\n")
