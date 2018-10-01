import time

t0 = time.time()

def numToDigits(n):
	d = []
	while n > 0:
		d.insert(0, n % 10)
		n /= 10
	return d

def findTidy(n):
	d = numToDigits(n)

	isTidy = True
	l = len(d)

	# find problem index
	index = -1
	for i in xrange(0, l-1):
		if d[i] > d[i+1]:
			index = i
			break
	
	if index == -1: return int(''.join(map(str, d)))

	# find actual start point in case of repeating numbers
	for i in xrange(0, index):
		if d[i] == d[index]:
			index = i
			break
	
	# subtract 1 from that index
	d[index] -= 1

	# change all digits to right of that index to 9
	for i in xrange(index+1, l):
		d[i] = 9

	return int(''.join(map(str, d)))

with open("/Users/andrewKyres/Downloads/google.in") as f:
	with open("/Users/andrewKyres/Downloads/google.out", "w+") as out:
		T = int(f.readline())
		for x in range(1, T+1):
			N = int(f.readline())
			out.write("case #%s: %d\n" % (x, findTidy(N)))

t1 = time.time()
print t1-t0