#!/usr/bin/env python

cases = int(raw_input())

for case in range(cases):
	line = raw_input().split()
	N = int(line[0])
	K = int(line[1])

	switches = [False] * N
	
	for i in range(K):
		for i in range(0, len(switches)):
			switches[i] = not switches[i]
			if switches[i]:
				break

	on = True
	for switch in switches:
		if not switch:
			on = False
			break

	print "Case #%d: " % (case + 1),
	if on:
		print "ON"
	else:
		print "OFF"
