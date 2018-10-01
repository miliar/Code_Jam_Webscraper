import sys

n = 0
l = 0

for line in sys.stdin:
	if n == 0:
		n = 1
		continue
	if l == 0:
		l = 1
		N = int(line)
		continue
	else:
		l = 0
	
	word = line.split()
	
	nword = []
	nsum = 0
	nsum2 = 0
	
	for i in range(N):
		nword += [int(word[i])]
		nsum += nword[i]
		nsum2 = (nsum2 | nword[i]) - (nsum2 & nword[i])

	if nsum2 == 0:
		outstr = str(nsum - min(nword))
	else:
		outstr = "NO"
	
	print "Case #" + str(n) + ": " + outstr
	n += 1
