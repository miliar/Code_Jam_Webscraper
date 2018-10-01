T = int(raw_input().strip())

def gcd_weird(a,b):
	print '   doing gcd(%d,%d)' % (a,b)
	if a==0 or b==0: return []
	if a>b:
		return [a/b] + gcd_weird(b, a % b)
	else:
		return [b/a] + gcd_weird(a, b % a)

def iwin(a,b):
	if a == b: return False
	big = max(a,b)
	small = min(a,b)
	if big > 2*small: return True
	return not iwin(big-small,small)
	

for case in range(1,T+1):
	count = 0
	(A1,A2,B1,B2) = map(int,raw_input().strip().split(' '))
	for i in xrange(A1,A2+1):
		for j in xrange(B1,B2+1):
			#print "%d,%d gives this sequence: %s" % (i,j,str(gcd_weird(i,j)))
			#if (max(i,j) >= 2 * min(i,j)):
			if iwin(i,j):
				#print "  %d,%d wins" % (i,j)
				count+=1




	print "Case #%d: %d" % (case,count)
