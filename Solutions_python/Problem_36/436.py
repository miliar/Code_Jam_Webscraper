NEEDLE = 'welcome to code jam'

N = input()
for case in xrange(N):
	haystack = raw_input()
	substrings = {}
	for i in xrange(1, len(NEEDLE) + 1):
		substrings[NEEDLE[:i]] = 0
	for c in haystack:
		if c in NEEDLE:
			for k in substrings.keys():
				if c == k:
					substrings[c] += 1
				if k + c in substrings and substrings[k]:
					substrings[k + c] += substrings[k]
	print 'Case #%d: %04d' % (case + 1, substrings[NEEDLE]%1000)

