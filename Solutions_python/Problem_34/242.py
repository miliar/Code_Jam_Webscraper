def lookup(DICT, D, L, pattern):
	letters = []
	pattern = pattern.strip()
	unclosed = False
	cand = []
	for i in range(len(pattern)):
		if pattern[i].islower():
			cand.append(pattern[i])
		if pattern[i] == '(':
			unclosed = True
		if pattern[i] == ')':
			unclosed = False
		if not unclosed:
			letters.append(cand[:])
			cand = []
	count = 0
	# print 'Lookup', pattern
	# print letters
	for i in range(D):
		match = True
		for j in range(L):
			if DICT[i][j] not in letters[j]:
				match = False
				break
		if match:
			count += 1
	return count


if __name__ == '__main__':
	INFILE = 'A-large.in'
	IN = open(INFILE)
	LINE = IN.readline()
	DATA = LINE.split()
	L = int(DATA[0]) #word length
	D = int(DATA[1]) #dictionary
	N = int(DATA[2]) #test cases
	DICT = []
	for i in range(D):
		LINE = IN.readline()
		DICT.append(LINE)
	for i in range(N):
		LINE = IN.readline()
		result = lookup(DICT, D, L, LINE)
		print 'Case #%d: %d'%(i+1, result)

