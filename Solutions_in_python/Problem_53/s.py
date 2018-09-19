l = int(raw_input())
for x in range(l):
	r = raw_input()
	re = [int(e) for e in r.split()]
	a = 2**re[0]
	b = re[1]+1
	if b%a==0:
		print "Case #%d: ON" % (x+1)
	else:
		print "Case #%d: OFF" % (x+1)
