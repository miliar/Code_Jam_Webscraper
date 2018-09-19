import sys
data = [x.strip() for x in sys.stdin.readlines()]

T = int(data.pop(0))
testcases = []
for elem in data:
	N, K = tuple(elem.split(' '))
	testcases.append((int(N), int(K)))


for case, NK in enumerate(testcases):
	N, K = NK
	snappers = [False] * N
	powered = 0

	for i in xrange(K):
		for j in xrange(powered, -1, -1):
			snappers[j] = not snappers[j]

		try:
			powered = snappers.index(False)
		except ValueError:
			powered = len(snappers) - 1

	light_on = (powered == len(snappers) - 1) and snappers[-1]
	print "Case #" + str(case + 1) + ": " + ("ON" if light_on else "OFF")
