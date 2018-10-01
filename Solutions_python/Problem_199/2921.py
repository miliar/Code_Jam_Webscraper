def flip(i):
	if(i=='-'):
		return '+'
	elif(i=='+'):
		return '-'

size=input()
for no in range(0,size):
	inp=raw_input()
	d=inp.split(" ")
	s=d[0]
	s=list(s)
	k=int(d[1])
	count=0
	flag=1
	for i in range(0,len(s)-k+1):
		if(s[i]=='-'):
			s[i]='+'
			for j in range(0,k-1):
				s[i+j+1]=flip(s[i+j+1])
			count=count+1
	for j in range(len(s)-k,len(s)):
		if(s[j]=='-'):
			flag=0
			break
	if(flag==0):
		print "Case #"+str(no+1)+": "+"IMPOSSIBLE"
	else:
		print "Case #"+str(no+1)+": "+str(count)