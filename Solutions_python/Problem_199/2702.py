def flip(char):
	if char == '+':
		return '-'
	else:
		return '+'

T = int(raw_input())
for t in range(T):
	pattern, flipper = raw_input().split(' ')
	flipper = int(flipper)
	pattern = list(pattern)
	flips = 0
	fixed = 0
	length = len(pattern)
	while True:
		while fixed<length and pattern[fixed]=='+':
			fixed+=1
		if fixed==length:
			print "Case #"+str(t+1)+":",flips
			break
		if fixed+flipper > length:
			print "Case #"+str(t+1)+": IMPOSSIBLE"
			break
		for i in range(fixed, fixed+flipper):
			pattern[i] = flip(pattern[i])
		flips+=1