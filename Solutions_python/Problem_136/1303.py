n = int(raw_input())

for i in range(1,n+1):
	line = raw_input().split()
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	
	# Seconds
	sec = 0.0
	# Cookies / second
	cps = 2.0
	
	while 1:
		# Seconds to finish if you don't build a farm
		sec1 = x / cps
		# Seconds to finish if you build a farm
		sec2 = (c / cps) + (x / (cps + f))
		if sec2 < sec1:
			sec += c / cps
			cps += f
		else:
			sec += sec1
			break
		#print sec1, sec2, sec
	
	str = "Case #%d: %.7f" % (i, sec)
	print str
	#print "---------------------"
			