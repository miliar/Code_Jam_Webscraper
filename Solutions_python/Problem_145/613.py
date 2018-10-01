import sys

filename = sys.argv[1]
f = open(filename, 'r')

numCases = int(f.readline())

for t in range(numCases):
	line = f.readline().strip().split('/')
	P = int(line[0])
	Q = int(line[1])

	if (Q & (Q-1)) != 0:
		print "Case #"+str(t+1)+": impossible"
		continue

	gen = -1
	frac = float(P)/float(Q)

	for n in range(1,41):
		if frac >= (1.0)/float(2**n):
			gen = n
			break

	if gen > -1:
		print "Case #"+str(t+1)+": "+str(gen)
	else:
		print "Case #"+str(t+1)+": impossible"