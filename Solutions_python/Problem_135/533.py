numTestCases = int(raw_input())


# print numTestCases


for n in xrange(numTestCases):
	# Read grid one data
	answerOne = int(raw_input())
	gridOneRow1 = map(int, raw_input().split())
	gridOneRow2 = map(int, raw_input().split())
	gridOneRow3 = map(int, raw_input().split())
	gridOneRow4 = map(int, raw_input().split())
	gridOne = [gridOneRow1, gridOneRow2, gridOneRow3, gridOneRow4]

	# print gridOne

	# Read grid two data
	answerTwo = int(raw_input())
	gridTwoRow1 = map(int, raw_input().split())
	gridTwoRow2 = map(int, raw_input().split())
	gridTwoRow3 = map(int, raw_input().split())
	gridTwoRow4 = map(int, raw_input().split())
	gridTwo = [gridTwoRow1, gridTwoRow2, gridTwoRow3, gridTwoRow4]

	# print gridTwo

	# Get possible answers
	gridOneNumbers = gridOne[answerOne-1]
	gridTwoNumbers = gridTwo[answerTwo-1]

	# print gridOneNumbers
	# print gridTwoNumbers

	# Case 1 - Unique number between two lists
	# Case 2 - No common number in lists (volunteer cheat)
	# Case 3 - Non unique number between lists (bad magic)
	count = 0
	for x in gridOneNumbers:
		for y in gridTwoNumbers:
			if x==y:
				number = x
				count = count + 1
	# print count

	if count == 0:
		print "Case #{}: {}".format(n+1, "Volunteer Cheated!")
	elif count == 1:
		print "Case #{}: {}".format(n+1, number)
	else:
		print "Case #{}: {}".format(n+1, "Bad magician!")
