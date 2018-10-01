t=int(input())
j=1
while(j<=t):
	r=int(input())
	i=1
	s=[]
	while(i<=4):
		if(i==r):
			s=map(int,raw_input().split(" "))
		else:
			x=raw_input()
		i+=1
	r1=int(input())
	i=1
	p=[]
	while(i<=4):
		if(i==r1):
			p=map(int,raw_input().split(" "))
		else:
			x=raw_input()
		i+=1
	count=0
	number=0
	for x in s:
		for y in p:
			if(x==y):
				count+=1
				number =x
	if(count==1):
		s="Case #"+str(j)+": "+str(number)
		print s
	elif(count==0):
		s="Case #"+str(j)+": Volunteer cheated!"
		print s
	else:
		s="Case #"+str(j)+": Bad magician!"
		print s
	j+=1
