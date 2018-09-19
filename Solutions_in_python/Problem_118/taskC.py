import sys
import math
def isPalindrom(n):
	print n
	s = str(n)
	L = len(s)
	if L == 1:
		return True
	lim = int(L/2)
	
	for i in range(lim):
		if s[i] != s[L-1-i]:
			return False
	return True
	
	


oF = open(sys.argv[1])
oF1 = open('taskCSol.txt','w')

T = int(oF.readline().strip())

for i in range(T):
	parts = oF.readline().strip().split()
	A = int(parts[0])
	B = int(parts[1])
	
	A_ = int(math.sqrt(A))
	B_ = int(math.sqrt(B))
	pal = 0
	print A_,B_
	
	while A_<=B_:
		if A_*A_ < A:
			A_=A_+1
			continue
		if isPalindrom(A_):
			if isPalindrom(A_*A_):
				pal=pal+1
		A_=A_+1
	oF1.write('Case #%d: %d\n'%((i+1),pal))
	
oF1.close()