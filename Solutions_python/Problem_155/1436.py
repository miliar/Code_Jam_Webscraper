#!/usr/bin/python
t=int(input())
for i in xrange(t):
	st=raw_input()
	n=0
	smax,string=st.split()
	sum=0
	for j in xrange(int(smax)+1):		
		sum+=int(string[j])
		if j >= sum:
			n+=1
			sum+=1
	print "Case #%d: %d" %(i+1 ,n)
