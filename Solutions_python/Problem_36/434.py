import sys

def count(search, string):
	if len(search) == 0:
		return 1;
	
	ret = 0

	while True:
		i = string.find(search[0])
		if i == -1:
			break
		string = string[i+1:]
		ret += count(search[1:], string)

	return ret

lines = int( sys.stdin.readline() )

for i in xrange(1, lines+1):
	line = sys.stdin.readline()
	print "Case #%d: %04d" % (i, count("welcome to code jam", line) % 10000)
