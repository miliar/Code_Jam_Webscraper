import sys
import re

reg1 = re.compile('\( *([0-9.]+)(.*)\)')
reg2 = re.compile(' *([a-z]+)(.*)')

def splitsub(value):
	parent = 0
	first = False
	for i in range(len(value)):
		if value[i] == '(':
			parent += 1
			first = True
		elif value[i] == ')':
			parent -= 1
			if parent == 0:
				return i+1
	print 'ERROR!!! ', value
	return -1

def maketree(data):
	m1 = reg1.match(data.strip())
	prob, subtree = m1.groups()
	prob = float(prob)
	opt = subtree.strip()
	if len(opt) == 0:
		return [prob]			# leaf
	else:
		m2 = reg2.match(opt)
		if m2 is None:
			print subtree
		feature, subtree = m2.groups()
		i = splitsub(subtree)
		lsub = maketree(subtree[0:i])
		rsub = maketree(subtree[i:])
		return [prob, feature, lsub, rsub]

def findprob(tree, features, p=1.0):
	if len(tree) == 1:
		return p*tree[0]		# leaf
	if features.has_key(tree[1]):
		return findprob(tree[2], features, p*tree[0])
	return findprob(tree[3], features, p*tree[0])

def solve(f):	# f file
	L = int(f.readline())
	data = "".join([f.readline() for x in range(L)])
	data = data.replace("\n", " ")
	tree = maketree(data)

	A = int(f.readline())
	animals = [f.readline() for x in range(A)]
	for animal in animals:
		res = animal.split(None, 2)
		if len(res) == 2:
			feats = dict()
		else:
			feats = res[2].split()
			feats = dict([(x, 0) for x in feats])
		p = findprob(tree, feats)
		print '%.7f' % p

f = open(sys.argv[1], 'r')
N = int(f.readline())
for i in range(N):
	print 'Case #%d:' % (i+1)
	solve(f)
f.close()
