def f():
	case = input()
	for i in range(case):
		size = raw_input()
		a = map(float,raw_input().split())
		b = map(float,raw_input().split())

		#print a
		#print b
		a.sort()
		b.sort()

		c=0
		bi = 0
		for blah in range(len(a)):
			if a[blah]>b[bi]:
				c+=1
				bi+=1
		c2=0
		ai=0
		for blah in range(len(b)):
			if b[blah]>a[ai]:
				c2+=1
				ai+=1
		#print c,len(b)-c2
		print ("Case #"+str(i+1)+ ": "+str(c) + " "+ str(len(b)-c2))



f()