def getTuples(str):
	char_list = []
	oldChar = str[0]
	current = 1
	for s in str[1:] + " ":
		if oldChar != s:
			char_list.append((oldChar, current))
			current = 0
			oldChar = s
		current += 1
	return char_list


def solve():
	is_invalid = False
	INVALID = "Fegla Won"
	N = int(raw_input())
	tuplesList = []
	firstTuple = getTuples(raw_input())
	tuplesList.append(firstTuple)
	count = 0
	for _ in xrange(1, N):
		tuples = getTuples(raw_input())
		if (len(firstTuple) != len(tuples)):
			is_invalid = True
		tuplesList.append(tuples)

	if is_invalid:
		return INVALID

	for i in xrange(len(tuplesList[0])):
		if tuplesList[0][i][0] != tuplesList[1][i][0]:
			return INVALID
		count += abs(tuplesList[0][i][1] - tuplesList[1][i][1])

	return count


T = int(raw_input())
for t in xrange(1, T + 1):
	print ("Case #%d: " % t ) + str(solve())