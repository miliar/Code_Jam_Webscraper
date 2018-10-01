o=int(raw_input())
for ot in range(o):
	a=raw_input()
	b=int(a)
	d=a
	for i in range(b,0,-1):
		c=list(str(i))
		c.sort()
		c=int(''.join(c))
		if c==i:
			d=i
			break
	print "Case #%d: %d" % (ot+1, d)
