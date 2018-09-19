import psyco
psyco.full()

lines = open("A-large.in").read().split("\n")

#print lines

#input
l, d, n = [int(x) for x in lines[0].split()]
#print l,d,n

#dictionary
w = lines[1:d+1]
	
#print w

def compute(inputWord):	
	global w
	w1 = w[:]
	for i in xrange(len(inputWord)):
		w1 = [x for x in w1 if x[i] in inputWord[i]]
	return len(w1)	
	
#list of empty words
words = []
for i in xrange(n):
	words.append([])

#n tests
output = []
for i in xrange(1, n+1):
	s =[]
	for c in lines[d+i]:
		if 'a'<=c<='z' and len(s)==0: words[i-1].append([c])
		elif c==")":
			words[i-1].append(s[1:])
			s = []
		else: s.append(c)
	if len(s)>0:
		words[i-1].append(s)
	counter = compute(words[i-1])
	print "Case #" + str(i) + ": " + str(counter)
	output.append( "Case #" + str(i) + ": " + str(counter) )

#print "\n".join(output)
open("result.txt","w").write( "\n".join(output) )
