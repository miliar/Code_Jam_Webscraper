class Tree:
	def __init__(self, weight, feature=None):
		self.feature = feature
		self.weight = weight
		self.left = None
		self.right = None

	def eval(self, features, p=1):
		p = p * self.weight
		if self.feature == None:
			return p
		if self.feature in features:
			return self.right.eval(features, p)
		else:
			return self.left.eval(features, p)
	def tostr(self):
		if self.feature:
			return "(%f %s %s %s)" % (self.weight, self.feature, self.right.tostr(), self.left.tostr())
		else:
			return "(%f)" % (self.weight)

class Tokeniser:
	def __init__(self, str):
		self.stuff = str.split()
		self.index = 0
	
	def peek(self):
		if self.index >= len(self.stuff):
			return None
		blah = self.stuff[self.index].strip()
		while not blah:
			self.index += 1
			blah = self.stuff[self.index].strip()
		if blah.startswith("("):
			return "("
		elif blah == ")":
			return ")"
		elif blah.endswith(")"):
			return blah[:-1]
		else:
			return blah

	def next(self):
		if self.index >= len(self.stuff):
			return None
		blah = self.stuff[self.index]
		while not blah.strip():
			self.index += 1
			blah = self.stuff[self.index]
		if blah.startswith("("):
			self.stuff[self.index] = blah[1:]
			if not self.stuff[self.index]:
				self.index += 1
			return "("
		elif blah == ")":
			self.index += 1
			return ")"
		elif blah.endswith(")"):
			a = blah.find(")")
			self.stuff[self.index] = blah[a:]
			return blah[:a]
		else:
			self.index += 1
			return blah

	def out(self):
		print self.stuff, self.index

def makeTree(tok):
	sym = tok.next()
	if sym == "(":
		weight = float(tok.next())
		tree = None
		if tok.peek() == ")":
			tree = Tree(weight)
		else:
			tree = Tree(weight, tok.next())	
			tree.right = makeTree(tok)
			tree.left = makeTree(tok)
		tok.next()
		return tree
	return Tree(1)

N = int(raw_input())
for i in xrange(N):
	print "Case #%d:" % (i+1)
	L = int(raw_input())
	treestr = ""
	for j in xrange(L):
		treestr += raw_input()

	tree = makeTree(Tokeniser(treestr))
	
	A = int(raw_input())
	for k in xrange(A):
		words = raw_input().split()
		name = words[0]
		features = words[2:]
		print "%.7f" %(tree.eval(features))

