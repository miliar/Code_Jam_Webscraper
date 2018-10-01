import sys

t = int(sys.stdin.readline())

count = 1

for line in sys.stdin:
	if count > t :
		break
	tokens = line.split()
	c = int(tokens[0])
	i = 1
	combine = dict()
	while i<=c:
		word = tokens[i]
		combine[(word[0],word[1])] = word[2]
		combine[(word[1],word[0])] = word[2]
		i+=1
	
	d = int(tokens[i])
	i += 1
	oppose = set()
	while i<=d+c+1:
		word = tokens[i]
		oppose.add( (word[0],word[1]) )
		oppose.add( (word[1],word[0]) )	
		i+=1
	
	n = int(tokens[i])
	i += 1

	stack = []

	for char in tokens[i]:
		stack.append(char)
		combining = True
		while len(stack) > 1 and combining:
			if (stack[-1], stack[-2]) in combine:
				stack.append(combine[stack.pop(), stack.pop()])
			else:
				combining = False
		if len(stack) > 1:
			clown = 0
			while clown < len(stack)-1:
				if (stack[-1], stack[clown]) in oppose:
					stack = []
				clown += 1 
	print "Case #" + str(count) + ": [",
	sys.stdout.softspace=0
	for char in stack[:-1]:
		print str(char) + "," ,
	if len(stack) > 0 :
		print str(stack[-1]),
		sys.stdout.softspace=0
	print "]"
	count+=1
print 
