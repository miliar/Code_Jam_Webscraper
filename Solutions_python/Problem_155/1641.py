t=input()
for i in xrange(t):
	[num,line]=raw_input().split(' ')
	m=int(num)
	
	need=0
	have=0
	for j in xrange(m+1):
		if j>have:
			need+=j-have
			have+=j-have
		have+=int(line[j])
		
	print 'Case #%d: %d' %(i+1, need)