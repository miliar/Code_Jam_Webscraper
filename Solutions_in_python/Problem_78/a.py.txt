import sys
try:
	t = input()
	#print t
	M = t+1
	while t>0:
		f1 = 0
		f2 = 0
		a = []
		s = raw_input()
		for i in s.split(' '):
			a.append(int(i))
		n = a[0]
		pd = a[1]
		pg = a[2]
		#print n, pd, pg
		x = 0
		lost = 0
		while n>0:
			if (pd*n)%100 == 0:
				x = n
				f1 = 1
				break;
			n = n-1
		lost = n-((pd*n)/100)
		while x<10**4:
			if (pg*x)%100 == 0:
				l1 = x-(pg*x)/100
				if f1 == 1:
					if l1 >= lost: 
						f2 = 1
						break;
			x = x+1
		a = []
		a.append('Case')
		#print a
		a.append('#'+str(M-t)+':')
		#print a
		if f1 == 1:
			if f2 == 1:
			#	print x,n
				a.append("Possible")
			else:
				a.append("Broken")
		else:
			a.append("Broken")
		print a[0], a[1], a[2]
		t = t-1
except:
	sys.exit(0)