import sys

def readnlines(file, n):
	ret = []
	for i in range(n):
		ret.append(file.readline().rstrip("\n\r"))
	return ret

def case(file, n):
	engines = {}
	for e in readnlines(file, int(file.readline())):
		engines[e] = False
	
	resets = 0
	for t in readnlines(file, int(file.readline())):
		engines[t] = True
		if all(engines.values()):
			resets += 1
			for k in engines:
				engines[k] = False
			engines[t] = True

	print "Case #%d: %d" % (n, resets)

f = file(sys.argv[1])
for i in range(int(f.readline())):
	case(f, i+1)
