T = int(raw_input())
for i in range(T):
	bla, digits = raw_input().split()
	total = 0
	answer = 0
	for index, digit in enumerate(digits):
		digit = int(digit)
		if total < index:
			answer += index - total
			total = index
		total += digit
	print "Case #%d: %d" % (i+1, answer)
		
