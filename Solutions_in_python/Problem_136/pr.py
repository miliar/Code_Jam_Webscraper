def solve(ca,fa,xa):
	cc = 2.0
	t1 = 0.0
	if ((xa-cc)!=0):
		while (xa/cc > (ca/cc + xa/(cc+fa))):
			t1 = t1 + (ca/cc)
			cc = cc + fa
		t1 = t1 + xa/cc
	else:
		t1 = 1.0
	
	cc  = 2.0
	#t.append(t1)	
	return t1


iFile = open('c://input.in','r')
oFile = open('c://output.out','w')
numOfCases = iFile.readline()
t = []
t1 = 0.0
cc = 2.0
c = 0
f = 0
x = 0

for i in range(int(numOfCases)):
	string = iFile.readline()
	print(string)
	c,f,x = string.split(' ')
	t.append(solve(float(c),float(f),float(x)))

for p in range(int(numOfCases)):
	oFile.write('Case #'+str(p+1)+': '+str(t[p])+"\n")