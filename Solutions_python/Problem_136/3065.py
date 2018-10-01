#!/usr/bin/python

import sys
	
if 1==1:#sys.stdin.readline().rstrip("\n")=='Input':
	count = int(sys.stdin.readline(),10)
	for i in range(0,count):
		cfx=sys.stdin.readline().split()

		c=float(cfx[0])
		f=float(cfx[1])
		x=float(cfx[2])
		cook=0
		rate=2
		time=0

		while cook!=x:
			buy=(c/rate)+(x/(rate+f))
			nobuy=(x/rate)
			
			if buy<nobuy:
				time=time+(cook+c)/rate
				rate=rate+f
			else:
				time=time+x/rate
				cook=x
			##print('buy',buy,'nobuy',nobuy)
			##print('time',time)
			##print('rate',rate)

		##print(c,f,x,time)
		print("Case #"+str(i+1)+": "+"{0:.7f}".format(time))

		

	
#End
