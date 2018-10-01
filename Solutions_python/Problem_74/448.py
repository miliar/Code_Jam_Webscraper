names = ['B', 'O']
indexes = []
pos = []
file = open("input.in")

def findNextMove(tokens, r):
	while(indexes[r] < len(tokens) and tokens[indexes[r]] != names[r]):
		indexes[r] += 2

line = file.readline()
caseNo = 1;
for line in file:
	indexes = [1, 1]
	pos = [1, 1]
	done = [1, 1]
	steps = 0;
	tokens = line.strip().split()
	if (len(tokens) == 1):
		continue

	while(indexes[0] < len(tokens) or indexes[1] < len(tokens)):
		for r in [0, 1]:
			if (done[r]):
				findNextMove(tokens, r)
				done[r] = 0

		pushed = 0
		for r in [0, 1]:
			if (indexes[r] >= len(tokens)):
				continue
			move = int(tokens[indexes[r] + 1])
			if (pos[r] != move):
				if (pos[r] < move):
					pos[r] += 1
				else:
					pos[r] += -1
			else:
				other = (r + 1) % 2
				if (pushed == 0 and indexes[other] > indexes[r]):
					done[r] = 1
					indexes[r] += 2
		steps += 1
	print "Case #%d: %d" % (caseNo, steps)
	caseNo += 1