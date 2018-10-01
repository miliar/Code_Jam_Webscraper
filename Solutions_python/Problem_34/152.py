import sys

args = sys.argv[1:]

inputfile = args[0]
outputfile = inputfile+'.out'

f = open(inputfile)

l1 = f.readline().strip()
print l1
ls1 = l1.split(' ')
L = int(ls1[0])
D = int(ls1[1])
N = int(ls1[2])

class PrefixTree:
	def __init__(self, c):
		self.c = c
		self.children = {}
	def add_child(self, cc):
		if not self.children.has_key(cc):
			cn = PrefixTree(cc)
			self.children[cc] = cn
			return cn
		else:
			return self.children[cc]
	def check(self, cc):
		return self.children.get(cc, None)

	def __str__(self):
		s = "%s" % self.c
		if len(self.children)>0:
			s += ": ["
			for k,v in self.children.iteritems():
				s +=str(v)
				s +=", "
			s += "]"
		return s
			
ROOT = PrefixTree('')

lang_set = set([])
lang_set_1 = [set()]*L
for i in range(L):
	lang_set_1[i] = set([])

for i in range(D):
	l = f.readline().rstrip('\r\n')
	print l
	if len(l)<>L:
		print "ERROR: a word should be of size %d. '%s'" % (L, l)
		sys.exit(1)
	lang_set.add(l)
	ptnode = ROOT
	for li, lv in enumerate(l):
		lang_set_1[li].add(lv)
		ptnode = ptnode.add_child(lv)
print "parsed words"

print lang_set_1

print ROOT

def count_pat(depth, pattern, pfnode):
	if depth>=L:
		return 1
	c = 0
	for p in pattern[depth]:
		cnode = pfnode.check(p)
		if cnode is not None: # not a valid word
			c += count_pat(depth+1, pattern, cnode)
		
	return c

fo = open(outputfile, 'w')
case_no = 0
for i in range(N):
	case_no += 1
	l = f.readline().rstrip('\r\n')
	print l
	patterns = [set()]*L
	pos = 0
	patpos = 0
	llen = len(l)
	while pos<llen:
		if l[pos]=='(':
			patterns[patpos] = []
			pos += 1
			while l[pos]<>')':
				patterns[patpos].append(l[pos])
				pos += 1
		else:
			patterns[patpos] = [l[pos]]
		#print patterns
		pos+=1
		patpos+=1
	print patterns
	count = 0
	failed = False
	for pi, pv in enumerate(patterns):
		found = False
		for pii in pv:
			if pii in lang_set_1[pi]:
				found = True
				break
		if not found:
			failed = True
			break
	if not failed:
		print "simple check failed, do recursive check"
		#for r in range(500):
		count = count_pat(0, patterns, ROOT)
	outstr = "Case #%d: %d" % (case_no, count)
	print outstr
	fo.write(outstr);
	fo.write('\n');
	
f.close()
fo.close()

print "Done. written to %s"% outputfile

