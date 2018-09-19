#! /usr/bin/env python

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

T = int(raw_input())
for t in xrange(T):
	[B, N] = map(int, raw_input().split())
	M = map(int, raw_input().split())
	# TimeTable = M[:]
	TimeTable = [0]*B
	if B > N:
		print "Case #%d:" % (t+1), N
		continue
	mlcm = lcmm(*M)
	batch = 0
	for x in M:
		batch = batch + mlcm/x
	# improve
	currentCustomer = (N / batch - 1) * batch
	# print currentCustomer
	while currentCustomer < N:
		Time = min(TimeTable)
		for x in xrange(0, B):
			if (TimeTable[x] - Time) == 0:
				currentCustomer = currentCustomer + 1
				TimeTable[x] = M[x]
				if currentCustomer == N:
					result = x+1
			else:
				TimeTable[x] = TimeTable[x] - Time
	print "Case #%d:" % (t+1), result
