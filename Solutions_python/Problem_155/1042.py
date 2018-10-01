import sys

num_cases = int(sys.stdin.readline())

def result(a):
	total = 0
	added = 0
	a = a.split()
	b = list(a[1])
	for i in xrange(0,int(a[0]) + 1):
		v = int(b[i])
		if (v > 0):
			while (total < i):
				added += 1
				total += 1
			total += v
	return str(added)
	


for i in range(1,num_cases+1):
	print "Case #" + str(i) + ": " + result(sys.stdin.readline())

