def binary(x):
	return bin(x)[2:]

def solve(candy):
	max = 2 ** len(candy)
	maxSeanVal = None
	for i in xrange(1,max-1):
		b = binary(i)
		while len(b) < len(candy):
			b = "0" + b
		patrick = [ candy[cnt] for cnt in xrange(len(b)) if b[cnt] == "1" ]
		sean = [ candy[cnt] for cnt in xrange(len(b)) if b[cnt] != "1" ]

		#print len(patrick), len(sean)

		patricksum1 = reduce(lambda tot, i: tot ^ i, patrick, 0)
		patricksum2 = reduce(lambda tot, i: tot ^ i, sean, 0)
		seansum = reduce(lambda tot, i: tot + i, sean, 0)

		#print "%10.10s %20.20s %10.10s %20.20s %10.10s %10.10s %s" % (i, sean, seansum, patricksum2, patrick, patricksum1, patricksum1 == patricksum2)
		if patricksum1 == patricksum2:
			if maxSeanVal == None:
				maxSeanVal = seansum
			elif seansum > maxSeanVal:
				maxSeanVal = seansum
	#print "------------------"
	return maxSeanVal

if __name__ == "__main__":
	print solve([1,2,3,4,5])
	print solve([3,5,6])
