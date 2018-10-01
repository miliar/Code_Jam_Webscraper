import sys

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def doit(input):
    X = int(input[0])
    R = int(input[1])
    C = int(input[2])



    if ((R * C) % X) != 0:
        return "RICHARD"

    if (X - 1) > R or (X-1) > C:
        return "RICHARD"
    else:
    	return "GABRIEL"


if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	t = int(f.readline())
	for _t in xrange(t):
		s = f.readline().split(' ')
		n = doit(s)
		print "Case #%d: %s" % (_t+1, n)
