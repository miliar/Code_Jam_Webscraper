from math import *
def max_possible_score(n):
	if (n == 0): 
		return (0, 0)
	return (ceil(n/3.0) + 1, ceil(n/3.0))

test_cases = int(raw_input())

for i in xrange(0, test_cases):
	x = 0
	case = [int(y) for y in raw_input().split()]
	n = case.pop(0) #number_of_googlers
	s = case.pop(0) #surprising
	p = case.pop(0)
	for t in case:
		m = max_possible_score(t)
#		print "Number: %d" % t
#		print m
		if m[1]>= p:
			x += 1
		elif m[0] >= p and s > 0:
			x +=1
			s -= 1


	print "Case #%d: %d" % (i+1, x)
