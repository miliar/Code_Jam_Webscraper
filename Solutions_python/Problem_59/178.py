#!/usr/bin/env python

# A binary tree class.
class Tree:
	def __init__(self, label):
		self.label = label
		self.nodes = {}

	def __iter__(self):
		return inorder(self)

	def addNode(self, node):
		self.nodes[node.label] = node


def inp():
	return [eval(x) for x in raw_input().strip().split()]

def addPath(tree, path):
	pal = path.split('/')
	pwd = tree
	mk = 0
	for dir in pal[1:]:
		#print dir
		if dir in pwd.nodes:
			pwd = pwd.nodes[dir]
		else:
			ndir = Tree(dir)
			pwd.addNode(ndir)
			mk += 1
			#print "makedir", dir
			pwd = pwd.nodes[dir]
	#print mk
	return mk


def solve(n, k):
	tree = Tree('')
	steps = 0
	for i in range(n):
		path = raw_input().strip()
		addPath(tree, path)
	
	for i in range(k):
		path = raw_input().strip()
		steps += addPath(tree, path)

	return steps

def solveCase():
	n, k = inp()
	steps = solve(n, k)
	return "%d" % steps

def main():
	[ncase] = inp()
	for i in xrange(ncase):
		print "Case #%d: %s" % (i+1, solveCase())

if __name__ == "__main__":
	main()


