import os, sys, random, math, itertools

def getSums(s):
	sums = {}
	subsets = set(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1,len(s)/2+1)))
	for x in subsets:
		total = sum(x)
		values = sums.get(total,[])
		if len(values)>0 and len(x) == len(list(set(x))):
			values.append(x)
			return values
		sums[total] = [x]
	return []
			
for tc in xrange(1,int(sys.stdin.readline())+1):
	nums = map(int,sys.stdin.readline().split())
	subsets = getSums(nums[1:])
	if len(subsets)<2:
		print 'Case #%s:' % tc, "Impossible"
	else:
		print 'Case #%s:' % tc
		for subset in subsets:
			print ' '.join(map(str,subset))
