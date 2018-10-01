f = open('A-small-attempt0.in', 'r')
f1 = open('mt_small.out', 'w')

#T=int(raw_input())
T=int(f.readline())

i=0
res=[]

i=0
while i < T:
	#n1=int(raw_input())
	n1=int(f.readline())
	
	for j in range(4):
		#s=raw_input().split()
		s=f.readline().split()
		if j+1 == n1:
			s1=[int(x) for x in s]
	#print "-------",s1
	
	#n2=int(raw_input())
	n2=int(f.readline())
	
	for j in range(4):
		#s=raw_input().split()
		s=f.readline().split()
		if j+1 == n2:
			s2=[int(x) for x in s]
	
	#print "-------",s2
	count=0
	val=0
	for k in s1:
		for j in s2:
			if k == j:
				count=count+1
				val=k
				#print k,j,count,"------"
	
	if count==1:
		res.append(str(val))
	elif count > 1 :
		res.append('Bad magician!')
	else :
		res.append('Volunteer cheated!')
	
	i=i+1

i=0
while i < T :
	f1.write("Case #"+str(i+1)+": "+res[i])
	#print "Case #"+str(i+1)+": "+res[i]
	if not i == (T-1):
		f1.write('\n')
	i=i+1
f.close()
f1.close()