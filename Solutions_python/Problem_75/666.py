import sys, itertools

def grouper(n, iterable, fillvalue=None):
	"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
	args = [iter(iterable)] * n
	return itertools.izip_longest(fillvalue=fillvalue, *args)

class Magicka():
	def __init__(self, comb, opp):
		self.element_list = []

		self.combine = {}
		for (a,b,c) in comb:
			self.combine[a+b] = c
			self.combine[b+a] = c
		
		#print self.combine
		
		self.opposed = {}
		for (a,b) in opp:
			self.opposed[a] = b
			self.opposed[b] = a
	
	def apply_combination(self):
		if len(self.element_list) < 2:
			return False
		a = self.element_list[-1]
		b = self.element_list[-2]
		c = a + b
		if c in self.combine:
			#print "applying ", a, "+", b, "->", self.combine[c]
			self.element_list = self.element_list[:-2]
			self.element_list.append(self.combine[c])
			return True
		return False
			
	def invoke(self, c):
		self.element_list.append(c)
		#print "invoke: ", c, self.element_list
		invoked = False
		while self.apply_combination():
			invoked = True
			
		if not invoked and c in self.opposed and self.opposed[c] in self.element_list:
			#print "opposed", self.opposed[c]
			self.element_list = []

filename = sys.argv[1]
f = open(filename)
o = open(filename + ".out", "wt")

num_tests = int(f.readline())
for t in range(1, num_tests+1):
	d = f.readline().split()
	#print d
	
	# read combinations
	c = int(d[0])
	d = d[1:]
	comb = []
	if c > 0:
		comb = d[:c]
		d = d[c:]
	
	# read opposing
	oc = int(d[0])
	d = d[1:]
	opp = []
	if oc > 0:
		opp = d[:oc]
		d = d[oc:]
	
	m = Magicka(comb, opp)
	
	# read invocation
	n = int(d[0])
	d = d[1:]
	for cur in d[0]:
		m.invoke(cur)
	o.write("Case #%d: [%s]\n" % (t, ", ".join(m.element_list)))
	print ", ".join(m.element_list)

o.close()