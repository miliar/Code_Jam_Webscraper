import sys

args = sys.argv[1:]

inputfile = args[0]
outputfile = inputfile+'.out'

f = open(inputfile)

l1 = f.readline().strip()
print l1
T = int(l1)

MINS=None	

def c_b(p, ri):
	c = 0
	for i in range(ri+1, len(p)):
		if p[i]:
			c += 1
		else:
			break
	for i in range(ri-1, -1, -1):
		if p[i]:
			c += 1
		else:
			break
	return c
def check(tor, p, d, s):
	if d<=0:
		global MINS
		if MINS is None or s<MINS:
			MINS=s
	else:
		for ri in tor:
			p[ri]=False
			s1 =s+c_b(p, ri)
			tor1 = [ tori for tori in tor if tori != ri ]
			check(tor1, p, d-1, s1)
			p[ri]=True
	

fo = open(outputfile, 'w')
case_no = 0
for i in range(T):
	case_no += 1
	l = f.readline().rstrip('\r\n')
	ls = l.split(' ')
	P = int(ls[0]); Q=int(ls[1])
	print P, Q
	c = [True]*P
	l = f.readline().rstrip('\r\n')
	tor = [ int(li)-1 for li in l.split(' ') ]
	print tor
	MINS = None
	check(tor, c, Q, 0)
	outstr = "Case #%d: %d" % (case_no, MINS)
	print outstr
	fo.write(outstr);
	fo.write('\n');
	
f.close()
fo.close()

print "Done. written to %s"% outputfile

