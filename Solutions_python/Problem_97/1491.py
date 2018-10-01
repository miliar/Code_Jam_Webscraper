import sys

with open(sys.argv[1]) as input:
	input.next()
	for case, line in enumerate(input, 1):
		low, high = map(int, line.strip().split(' '))
		middle = (high - low) // 2 + low
		
		result = 0
		seen = set()
		for num in xrange(low, high + 1):
			strnum = str(num)
			if len(set(strnum)) == 1:
				continue
			for offset in xrange(1, len(strnum)):
				if strnum[offset] != '0':
					new = int(strnum[offset:] + strnum[:offset])
					if num < new and low <= new <= high:
						result += 1
						seen.add((num,new))		
		print 'Case #%s: %s' % (case, len(seen))