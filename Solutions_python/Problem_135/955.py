readArgs = lambda : raw_input().strip().split()
readInts = lambda : map(int, readArgs())
readInt = lambda : readInts()[0]

for T in range(1, readInt() + 1):
	r = readInt() -1
	i = set([readInts() for _ in range(4)][r])
	r = readInt() - 1
	j = set([readInts() for _ in range(4)][r])
	f = i & j
        print 'Case #%d:' % T,
	if len(f) == 1:
		print f.pop()
	elif not f:
		print 'Volunteer cheated!'
	else:
		print 'Bad magician!'

