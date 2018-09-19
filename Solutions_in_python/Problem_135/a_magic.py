import sys

def check_magic(l1, l2):
	l1 = [int(x) for x in l1.split()]
	l2 = [int(x) for x in l2.split()]
	card = None
	for c1 in l1:
		for c2 in l2:
			if c1 == c2:
				if card == None:
					card = c1
				else:
					return "Bad magician!" # more than 1 card
	
	if card == None:
		return "Volunteer cheated!"
	else:
		return str(card)

if __name__ == "__main__":
	f = sys.stdin
	T = int(f.readline())
	for i in xrange(T):
		first = int(f.readline()) - 1
		lines1 = [f.readline() for l in xrange(4)]
		second = int(f.readline()) - 1
		lines2 = [f.readline() for l in xrange(4)]
		print "Case #%d: %s" % (i + 1, check_magic(lines1[first], lines2[second]))
		