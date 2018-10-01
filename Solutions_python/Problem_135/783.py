t=input()
for tt in range(t) :
	n1=input()
	m1=[raw_input().split() for i in range(4)]
	n2=input()
	m2=[raw_input().split() for i in range(4)]
	num = set(m1[n1-1]) & set(m2[n2-1])

	if len(num)==1 :
		x=''.join(num)
	elif len(num)==0 :
		x="Volunteer cheated!"
	else :
		x="Bad magician!"
	print "Case #%d:"%(tt+1),x
	
