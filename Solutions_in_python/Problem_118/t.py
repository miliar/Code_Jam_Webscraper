import sys,math

T=sys.stdin.readline()
T=int(T)

def isPalin(t):
	s=str(t)
	for i in range(0, len(s)/2):
		if s[i]!=s[len(s)-1-i]:
			return False
	return True


for C in range(1,T+1):
	sum=0
	line=sys.stdin.readline().split()
	A=int(line[0])
	B=int(line[1])
	for t in range(int(math.sqrt(A-1)),int(math.sqrt(B+1))+1):
		if isPalin(t) and t*t>=A and t*t<=B and isPalin(t*t):
			sum+=1
	print 'Case #%d: %d' % (C, sum)

