def check(na,ke):
	for i in xrange(len(na)):
		if na[i] < ke[i]:
			return False
	return True

t=int(raw_input())
for x in xrange(t):
	n = int(raw_input())
	na,ke = [[float(i) for i in raw_input().split()] for j in xrange(2)]
	win = 0
	na1 = sorted(na)
	ke1 = sorted(ke)
	# print na
	# print ke
	while check(na1,ke1) == False:
		del na1[0]
		del ke1[-1]
	co = 0
	na = sorted(na)
	ke = sorted(ke)
	for i in xrange(len(na)):
		if na[-1] > ke[-1]:
			co += 1
			del na[-1]
			del ke[0]
		else:
			del na[-1]
			del ke[-1]
	print "Case #%s:"%(x+1),len(na1),co