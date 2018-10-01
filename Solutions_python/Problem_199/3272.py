t = int(raw_input())
for i in xrange(1, t + 1):
	line = str(raw_input())
	line = line.split(' ')
	s = list(line[0])
	k = int(line[1])
	if '-' not in s:
		print "Case #{}: {}".format(i, 0)
	else:
		result = 0
		j = s.index('-')
		end = len(s)
		while j <= end - k and j != -1:
			for x in xrange(j, j+k):
				if s[x] == '-':
					s[x] = '+'
				else:
					s[x] = '-'
			result += 1
			if '-' in s:
				j = s.index('-')
			else:
				j = -1
		if '-' in s:
			print "Case #{}: IMPOSSIBLE".format(i)
		else:
			print "Case #{}: {}".format(i, result)