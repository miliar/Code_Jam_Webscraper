t=input()

a=set()
b=set()
c=set()

for j in xrange(t):
	
	a.clear()
	b.clear()
	c.clear()

	p1=input()

	p1-=1	

	for i in xrange(4):
		temp=raw_input()
		if (i==p1): 
			for z in temp.split(): a.add(int(z))

	p2=input()
	
	p2-=1

	for i in xrange(4):
		temp=raw_input()
		if (i==p2): 
			for z in temp.split(): b.add(int(z))


	c=a.intersection(b)
	temp=len(c)


	print "Case #" + str(j+1) + ":",

	if(temp==0): print "Volunteer Cheated!"
	elif(temp==1): print c.pop()
	else: print "Bad Magician!"

