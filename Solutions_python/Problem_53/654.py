cases = int(input())
for i in range(1,cases+1):
	n, k = raw_input().split(' ')
	n = int(n)
	k = int(k)
	if ((k>0) and ((k+1)%(2**n)== 0)):
		out = "ON"
	else:
		out = "OFF"
	print "Case #%d: %s" % (i, out)