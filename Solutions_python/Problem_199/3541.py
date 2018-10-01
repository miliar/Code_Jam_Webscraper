def compute(tmp):
	pan, K = tmp.split(' ')
	K = int(K)
	pan = list(pan)
	count = 0
	for x in xrange(0,len(pan)-K+1):
		if pan[x] == '-':
			count += 1
			for j in xrange(x,x+K):
				if pan[j] == '-':
					pan[j] = '+' 
				else:
					pan[j] = '-'
				
	for x in xrange(len(pan)-K, len(pan)):
		if pan[x] == '-':
			return 'IMPOSSIBLE'

	return count
n = int(raw_input())
for i in xrange(1, n+1):
	tmp = raw_input()
	print "Case #"+str(i)+": "+ str(compute(tmp))