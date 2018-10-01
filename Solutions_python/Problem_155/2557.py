from sys import stdin

count = (int)(stdin.readline())

for i in range(count):
	line = stdin.readline().split(' ')
	smax = (int)(line[0])

	ses = [ (int)(x) for x in list(line[1].rstrip()) ]

	extra_persons = 0
	persons = ses[0]
	
	for k in range(1,smax+1):
		
		if (persons + extra_persons < k):
			extra_persons += k - persons - extra_persons
		
		persons += ses[k]
	
	print 'Case #%d: %d' % (i+1, extra_persons)
		
