import math

cases = input()

for t in range( 1, cases + 1 ):
	rcw = raw_input()
	
	r, c, w = rcw.split()
	r = float(r)
	c = float(c)
	w = float(w)
	
	# print 'r',r
	# print 'c',c
	# print 'w',w
	
	# print math.ceil(c/w)
	# print r*math.ceil(c/w)
	# print (r*math.ceil(c/w))+(w-1)
	print "Case #" + repr(t) + ":", int(r*math.ceil(c/w)+(w-1))
	