#Read input file
import sys
from nextNum import nextNum

def main(fileName):
	setting, data = fileOpen(fileName)
	i = 1
	for d in data:
		result = nextNum(d)
		#print result
		print "Case #%d: %d" % (i ,result)
		i += 1
		if i > setting:
			break

def fileOpen(fileName):
	f = open(fileName)
	i = 0
	data = []
	setting = f.readline()[:-1]
	for line in f:
		data.append(line[:-1])
		#print line[:-1]
		i += 1
		if i >= int(setting): break
	return setting,data

if __name__ == "__main__":
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		#import doctest
		#doctest.testmod(verbose=True)
		print "usage: exefile inputfile"
