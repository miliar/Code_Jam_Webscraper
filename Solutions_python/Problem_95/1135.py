d = {'a': 'y', 'b': 'n', 'c': 'f', 'd': 'i', 'e': 'c', 'f': 'w', 'g': 'l', 'h': 'b', 'i': 'k', 'j': 'u', 'k': 'o', 'l': 'm', 'm': 'x', 'n': 's', 'o': 'e', 'p': 'v', 'q': 'z', 'r': 'p', 's': 'd', 't': 'r', 'u': 'j', 'v': 'g', 'w': 't', 'x': 'h', 'y': 'a', 'z': 'q', ' ': ' '}

d_r = dict((v,k) for k, v in d.iteritems())

def translate(googlerese):
	result = ''
	for letter in googlerese:
		result += d_r[letter]
	return result

infile = open('A-small-attempt0.in')
outfile = open('A-small-attempt0.out', 'w')

caseId = 1
seenFirstLine = False
numCases = 0

for line in infile:
	line = line.strip()
	if not seenFirstLine:
		numCases = int(line)
		seenFirstLine = True
		continue
	else:
		outfile.write("Case #" + str(caseId) + ": " + translate(line) + '\n')
		caseId +=1

infile.close()
outfile.close()

if not numCases == caseId-1:
	print "WATCH OUT ... expected " + str(numCases) + " cases but saw " + str(caseId-1)
