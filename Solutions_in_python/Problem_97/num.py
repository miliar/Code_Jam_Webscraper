T = input()

for t in range(T):
	data = raw_input().split()
	a = int(data[0])
	b = int(data[1])
	count = dict()

	if a/10 == 0: 
		print("Case #%d: %d" % (t+1,0))
		continue
	else:
		for value in range(a,b+1):
			s = str(value)
			for i in range(1,len(s)):
				newvalue = int(s[i:]+s[:i])
				if newvalue <= b and newvalue > value : 
					count[(newvalue,value)] = 0
			
					
	
	print("Case #%d: %d" % (t+1,len(count)))