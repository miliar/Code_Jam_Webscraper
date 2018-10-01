#!/usr/bin/python

T = int(raw_input())
for t in range(T):
	n, k = tuple([int(i) for i in raw_input().split()])
	on = True
	for i in range(n):
		if k % 2 == 0:
			on = False
		k /= 2
		
	if on:
		print "Case #" + str(t + 1) + ": ON"
	else:
		print "Case #" + str(t + 1) + ": OFF"
	