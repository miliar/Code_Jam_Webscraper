import math
import sys

def checkPal(n):
	s = str(n)
	parity = len(s)%2
	s1 = s[0:len(s)/2]
	if parity==0:
		s2 = s[len(s)/2:]
	else:
		s2 = s[len(s)/2+1:]
	return s1 == s2[::-1]
		

f = open(sys.argv[1], 'r')
cases = int(f.readline())
for i in range(0,cases):
	l = f.readline()
	a = int(l.split(' ')[0])
	b = int(l.split(' ')[1])
	o = 0
	for j in range(a,b+1):
		sqj = math.sqrt(j)
		if(math.modf(sqj)[0] == 0):
			if( checkPal(j) and checkPal(int(sqj))):
				o+=1
			
	print "Case #"+str(i+1)+": "+str(o)
	

	

