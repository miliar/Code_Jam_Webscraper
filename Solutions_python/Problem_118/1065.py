import math

def isFair(n):
	s=str(n)
	n=0
	l=len(s)
	while n<l/2:
		if s[n]!=s[l-1-n]:
			return False
		n+=1
	return True
	
def isSquare(n):
	t=math.sqrt(n)
	if t==int(t):
		return True
	return False

def isExpt(n):
	if isFair(n) and isSquare(n):
		return isFair(int(math.sqrt(n)))
	else:
		return False

def foo():
	t = input()
	for n in xrange(t):
		x, y = map(int, raw_input().split())
		ans=0
		for t in xrange(x, y+1):
			if isExpt(t):
				ans+=1
		print 'Case #%d: %d' % (n+1, ans)
		#return
	
if __name__ == '__main__':
	foo()


