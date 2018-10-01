for _ in range(input()):
	s="Case #"+str(_+1)+": "
	input()
	c=map(int,raw_input().split())
	if reduce(lambda x,y:x^y, c)!=0:
		s+="NO"
	else:
		s+=str(sum(c)-min(c))
	print s

