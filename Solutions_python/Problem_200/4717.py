def solution(input, iteration):
	answer = 0
	iterFlag = True

	while iterFlag:
		inputString = str(input)
		flag = False
		for i in range(len(inputString) - 1):
			if inputString[i] > inputString[i+1]:
				flag = True
				break
		
		if flag:
			input -= 1
		else:
			answer = inputString
			iterFlag = False

	return "Case #" + str(iteration) + ": " + str(answer)




# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [int(s) for s in raw_input().split(" ")]
  print solution(n[0], i)

  #print "Case #{}: {} {}".format(i, n + m, n * m)




