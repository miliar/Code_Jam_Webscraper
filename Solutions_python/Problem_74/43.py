# -*- coding: utf-8 -*-


T = int(raw_input())

for x in range(1,T+1):
	
	bp,bt = 1,0		# last at position 1, at time 0
	op,ot = 1,0
	t = 0
	
	
	line = raw_input().split()
	N = int(line.pop(0))
	for i in range(N):
		who = line.pop(0)
		where = int(line.pop(0))
		if who=='B':
			dist = abs(where-bp)
			t = max(bt+dist, t)	# prep time
			t += 1	#press button
			bp = where
			bt = t
		elif who=='O':
			dist = abs(where-op)
			t = max(ot+dist, t)	# prep time
			t += 1	#press button
			op = where
			ot = t
		else:
			raise Exception('wut')
		
	
	
	print "Case #"+str(x)+": "+str(t)














