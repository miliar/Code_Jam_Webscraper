N = int(raw_input())
for i in xrange(N):
	nums = map(int, raw_input().split())
	T = nums[0]
	S = nums[1]
	p = nums[2]
	length = len(nums)
	count_satisfy = 0
	count_surprising = 0
	unavilable = 0
	#scores = [0] * (length - 3)
	#for j in xrange(3, length): scores[j - 3] = nums[j]
	#scores.sort()
	#is_satisfy = [False] * (length - 3)
	for j in xrange(3, length):
		if nums[j] >= p:
			count_satisfy += 1
			remainder = nums[j] % 3
			quotient = nums[j] / 3
			if remainder == 0:
				if p - quotient == 1:
					count_surprising += 1
				elif p - quotient > 1:
					unavilable += 1
			elif remainder == 1:
				if p - quotient > 1:
					unavilable += 1
			elif remainder == 2:
				if p - quotient == 2:
					count_surprising += 1
				elif p - quotient > 2:
					unavilable += 1
	res = 0
	if count_surprising > S:
		res = count_satisfy - (count_surprising - S)
	else:
		res = count_satisfy
	res -= unavilable
	print 'Case #%d: %d' % (i + 1, res)
	#print '%d %d %d' % (count_satisfy, count_surprising, res) 
