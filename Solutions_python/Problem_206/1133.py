

t = int( input() )
for testcase in  range (1, t+1):
	d, n = [int(x) for x in input().split() ]
	maxT = 0
	for i in range (n):
		k, s = [float(x) for x in input().split()]
		time = (d-k) / float(s)
		maxT = max( maxT, time)
	
	print ('Case #{0:d}: {1:6.7f}'.format(testcase, d/maxT) )
