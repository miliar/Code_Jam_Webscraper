q = input()

for i in range(1,q+1):
	p = 2.0
	nums = raw_input().split()
	c = float(nums[0])
	b = float(nums[1])
	x = float(nums[2])
	t = c / p

	while (x-c)*(p+b) > x*p :
		p += b
		t += c / p

	t += (x-c)/p

	print "Case #%d: %.8Lf" % (i,t)
