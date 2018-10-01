def result(t):
	str = raw_input().split()
	N = int(str[0])
	S = int(str[1])
	p = int(str[2])
	sums = range(N)
	for i in range(N):
		sums[i] = int(str[i+3])
	
	ans = 0
	sup = S
	sums.sort()
	for i in range(N):
		x1 = sums[i]/3
		x2 = (sums[i]-x1)/2 
		x3 = sums[i]-x1-x2
		if sup < N-i-1 and sup > 0:
			#print "logo"
			if (x2==x3): # x1=x2=x3 not surprised by default
				if x3==p-1 and x3 != 0:
					x3+=1
					x2-=1
					sup-=1

			if (x1 != x2 and x2 != x3): # surprised by default
				sup-=1
	
			if x3 >=p:
				ans+=1
		else:
			#print "pogo",ans,sup
			if x3==x2 and x3 != 0 and sup > 0:
				x3+=1
				x2-=1
				sup-=1
				
			else:
				if x1==x2 and x2 != 0 and sup > 0:
					x2+=1
					x1-=1
					sup-=1
					
				if x1 != x2 and sup > 0:
					sup-=1
					
			if x3 >= p:
				ans+=1
				
		#print x1,x2,x3

	print "Case #%d: %d" %(t,ans)	
		
t = int(raw_input())
for i in range(t):
        result(i+1)
