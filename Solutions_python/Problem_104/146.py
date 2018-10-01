import sys
debug = sys.stdout

sys.stdin  = open('C-small.in')
sys.stdout = open('C.out', 'w')

def duplicateSum(l):
	sums = {0:[]}
	for x in l:
		nextResultSet = {}
		for triedsum, triedset in sums.iteritems():
			nextsum = triedsum + x
			nextSet = triedset + [x]
			nextResultSet[nextsum] = nextSet
			if nextsum in sums:
				return sums[nextsum], nextSet
		sums.update(nextResultSet)

def solve(numbers):
	sums = duplicateSum(numbers)
	return sums

	#for s1 in permute(numbers):
	#	for s2 in permute(numbers):
	#		if s1 != s2 and s1 and s2 and sum(s1) == sum(s2):
	#			return s1, s2

for i in xrange(input()):
	numbers = [int(x) for x in raw_input().split(' ')]
	numbers = set(numbers[1:20])

	print 'Case #%d:' % (i + 1)
	solution = solve(numbers)
	if solution:
		print ' '.join(str(n) for n in solution[0])
		print ' '.join(str(n) for n in solution[1])
	else:
		print "Impossible"


	#print 'Case #%d: %s' % (i+1, 456)