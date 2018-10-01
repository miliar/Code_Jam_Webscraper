import sys
import re
import string

def skipspace(tree, x):
	while tree[x] in string.whitespace:
		x+=1
	return x
	
def readtoken(tree, x):
	x = skipspace(tree, x)
	if tree[x] == ')' :
		return (x+1, ')')
	line =''
	while not tree[x] in string.whitespace and tree[x] != ')':
		line += tree[x]
		x+=1
#	print line
	return (x, line)
	
def readtree(tree, x):
	x = skipspace(tree, x)
	x += 1 # '('
	(x, p) = readtoken(tree, x)
	p = float(p)
	(x,line) = readtoken(tree, x)
	if line == ')':
		return (x, [p])
	else:
		(x, left) = readtree(tree, x) 
		(x, right) = readtree(tree, x)
		x = skipspace(tree,x)
		x+=1
		return (x, (p, line, left, right))

N = int(sys.stdin.readline())
for case in range(N):
	print "Case #%d:" % (case+1)
	L = int(sys.stdin.readline())
	tree = ''
	for l in range(L):
		tree += sys.stdin.readline()
	A = int(sys.stdin.readline())
	caps = dict()
	ani = []
	for a in range(A):
		c = sys.stdin.readline().rstrip().split(' ')
		ani.append(c[0])
		caps[c[0]] = set(c[2:])
	(x, T) = readtree(tree, 0)
	for an in ani:
		p = 1.0
		zz = T
		while True:
#			print zz
#			print p
			p = p * zz[0]
			if len(zz) > 1:
				cap = zz[1]
				if cap in caps[an]:
					zz = zz[2]
				else:
					zz = zz[3]
			else:
				break
		print "%.8f" % p