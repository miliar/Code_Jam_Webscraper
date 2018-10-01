import sys,itertools

f = open(sys.argv[1], "r")
T = int(f.readline())

for c in range(T):
	i = map(int,f.readline().split())
	N = i[0]
	i = i[1:]
	d = dict([])
	stopnow = False
	for x in range(0, len(i)+1):
		for subset in itertools.combinations(i,x):
			s=sum(subset)
			if s in d:
				print "Case #" + str(c+1) + ": "
				print " ".join(map(str,subset))
				print " ".join(map(str, d[s]))
				stopnow = True
				break
			else:
				d[sum(subset)]=subset
		if(stopnow):
			break	
