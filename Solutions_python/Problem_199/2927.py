testcase_count = int(input())
for testcase_index in range(testcase_count):
	s, k = input().split()
	s = list(s)
	k = int(k)
	flips_required = 0
	#print("%s %d" % (s, k))
	for i in range(len(s) - k + 1):
		if s[i] == '-':
			flips_required += 1
			for flip_index in range(i, i + k):
				s[flip_index] = '+' if s[flip_index] == '-' else '-'
			#print(s, flips_required)
	for i in range(len(s) - k + 1, len(s)):
		if s[i] == '-':
			flips_required = -1
	print("Case #%d: %s" % (testcase_index + 1, flips_required if flips_required >= 0 else "IMPOSSIBLE"))
	
