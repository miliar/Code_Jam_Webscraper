import sys

data = [x.strip() for x in open(sys.argv[1])]

T = int(data.pop(0))
for t, line in enumerate(data):
	A, B = (int(x) for x in line.split(' '))
	total = 0
	counted = set()
	while A < B:
		s = str(A)
		for i in xrange(len(s) - 1):
			s = s[1:] + s[0]
			v = int(s)
			if v > A and v <= B:
				if (A, v) not in counted:
					total += 1
					counted.add((A, v))				
		A += 1
	print "Case #%d: %d" % ((t+1), total)