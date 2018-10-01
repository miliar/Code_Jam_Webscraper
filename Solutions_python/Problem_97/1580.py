def rotate(s,n):
	for i in xrange(n):
		s=s[-1:]+s[:-1]
    	return s 

t=int(raw_input())
for testCase in xrange(t):
	count=0
	a,b=map(int,raw_input().split())
	li=[0]*b
	s=set([tuple([0,0])])
	for n in xrange(a,b):
		string=str(n)
		le=len(string)
		string=rotate(string,1)
		i=int(string)
		le2=len(str(i))
		for x in xrange(le-1):
			#
			if i<=b and i>=a and i!=n and le==le2 and (tuple([n,i]) not in s ) :
				count+=1
				#print n,i
				#print n,i
				s=s.union([tuple([n,i])])
				s=s.union([tuple([i,n])])
			string=rotate(string,1)
			i=int(string)
			le2=len(str(i))
	#print tuple([101,110]) not in s
	print "Case #"+str(testCase+1)+":",count
