#!/usr/bin/env python


for i in range(int(raw_input())):
	print 'Case #{}:'.format(i + 1),
	X, R, C = map(int, raw_input().split())
	breaker = min(R, C) + 1
	if X + 1 - breaker >= breaker:
		#print 'rotation'
		print 'RICHARD'
	elif X >= 4 and R * C <= 8:
		print 'RICHARD'
	elif X > R and X > C:
		#print 'wide'
		print 'RICHARD'
	elif (R * C) % X:
		#print 'modfail'
		print 'RICHARD'
	elif X >= 7:
		#print 'hole'
		print 'RICHARD'
	else:
		print 'GABRIEL'
