#!/usr/bin/python2
n = int(input())
count = 1
while n > 0:
	n -= 1
	x = raw_input()
	num = x.split()
	c = float(num[0])
	f = float(num[1])
	x = float(num[2])
	cf = 0

	ft = c / (f*cf + 2)
	ft1 = ft + x / (f*(cf+1) + 2)
	xt = x / (f*cf + 2)
	if xt < ft1:
		print("Case #"+str(count)+": " + "%.7f" % xt)
	else:
		tt = 0
		while xt > ft1:
			cf += 1
			tt += ft
			ft = c / (f * cf + 2)
			ft1 = ft + x / (f*(cf+1) + 2)
			xt = x / (f * cf + 2)	
		tt += x / (f * cf + 2)
		print("Case #"+str(count)+": " + "%.7f" % tt)
	count += 1
