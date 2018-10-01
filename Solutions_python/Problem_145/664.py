def elf(p,q):
	count = 0
	temp = q
	while temp > 2:
		if temp % 2 != 0:
			return "impossible"
		else:
			temp = temp / 2
	while p/q < 1:
		count += 1
		p = p * 2
	return str(count)

f = open('A-small-attempt1.in')
no = int(f.readline())
for i in range(no):
	p, q = f.readline().strip().split('/')
	print "Case #%d: %s" % (i+1, elf(int(p),int(q)))