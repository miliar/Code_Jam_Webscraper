f = open("A-small-attempt1.in", "r")
lines = f.readlines()


def function(a, A, b, B):
	possible1 = A[a - 1].split()
	#print possible1
	possible2 = B[b - 1].split()
	#print possible2
	wut = set(possible1).intersection(possible2)
	#print wut
	if len(wut) == 1:
		return list(wut)[0]
	elif len(wut) > 1:
		return "Bad magician!"
	elif len(wut) < 1:
		return "Volunteer cheated!"

for i in xrange(int(lines[0])):
	print "Case #%d: %s"% (i+1, function(int(lines[10*i + 1]), [lines[10*i+2], lines[10*i + 3], lines[10*i + 4], lines[10*i+ 5]], int(lines[10*i +6]), [lines[10*i+7], lines[10*i + 8], lines[10*i + 9], lines[10*i+ 10]]))