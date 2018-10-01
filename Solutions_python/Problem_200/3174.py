testcase_count = int(input())
for testcase_index in range(testcase_count):
	N = int(input())
	for n in range(N, 0, -1):
		#check if tidy
		s = str(n)
		tidy = True
		digit = '0'
		for i in range(len(s)):
			if s[i] < digit:
				tidy = False
				break
			digit = s[i]
		if tidy:
			break
		
		
	
	
	
	print("Case #%d: %d" % (testcase_index + 1, n))
	
