input = open('A-large.in', 'r')
output = open('A-large.out', 'w')
for i, line in enumerate(input):
	try:
		(n, k) = map(int, line.split(' '))
	except:
		continue
	if k % (2**n) == 2**n - 1:
		print >>output,"Case #%d: %s" % (i, "ON")
	else:
		print >>output,"Case #%d: %s" % (i, "OFF")

output.close()
