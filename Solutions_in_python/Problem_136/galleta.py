import sys


def resuelve2(tc,C,F,X):
	print C,F,X
	if F>0:
		gb = X/F-C
	else:
		gb = 1
	
	#	velocidad,tiempo
	s = (2.0,0)
	fin = 0
	if gb > 0:
		while fin==0:
			print s
			t1 = X/(s[0]+F)
			t2 = X/s[0]
			print "--------->",(t1+C/s[0]),t2
			if (t1+C/s[0])<t2:
				s=(s[0]+F,s[1]+C/s[0])		
			else:
				s=(s[0],s[1]+t2)
				fin = 1
	else:
		t3 = X/2.0
		s=(2.0,t3)
	print "Case #"+str(tc)+": "+ ('%.5f' % s[1])
		
def resuelve(tc,C,F,X):
	#print C,F,X	
	#	velocidad,tiempo
	s = (2.0,0)
	fin = 0
	while fin==0:
		#print s
		t1 = X/(s[0]+F)
		t2 = X/s[0]
		#print "--------->",(t1+C/s[0]),t2
		if (t1+C/s[0])<t2:
			s=(s[0]+F,s[1]+C/s[0])		
		else:
			s=(s[0],s[1]+t2)
			fin = 1

	print "Case #"+str(tc)+": "+ ('%.7f' % s[1])		
		

def read_board():
	a = sys.stdin.readline().rstrip().split(' ')
	a = [float(x) for x in a]
	return (a[0],a[1],a[2])


	
#--------------------------------------------------	

T = int(sys.stdin.readline().rstrip())
for tc in range(T):	
	(C,F,X) = read_board()
	resuelve(tc+1,C,F,X)