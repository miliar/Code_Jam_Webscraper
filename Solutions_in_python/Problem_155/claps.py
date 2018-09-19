T = int(raw_input())
for case in range(T):
	smax,slist = map(str,raw_input().split())
	smax = int(smax)
	slist = [int(i) for i in str(slist)]
	total = 0
	friends = 0
	for level in range(smax+1):
		if(level <= total or slist[level]==0):
			total = total + slist[level]
		else:
			friendsneeded = level - total
			friends = friends + friendsneeded
			total = total + friendsneeded + slist[level]
	print "Case #%d: %d" % (case+1, friends)