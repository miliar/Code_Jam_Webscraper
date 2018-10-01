t=int(raw_input())
for i in xrange(t):
	c,f,x=map(float,raw_input().split())
	a=2.0
	mxt=x/a
	mit =0.0
	n=1
	while(True):
		mit = mit +c/a
		if(mxt < mit +x/(a+f)):
			break
		else:
			mxt = mit +x/(a+f)
		a=a+f
	print "Case #%d: %f" %(i+1,mxt)
		
