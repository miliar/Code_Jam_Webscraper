# coding: utf8
# rozwiązanie ?
import sys

AND	= 1
OR	= 0
L	= None

if len(sys.argv) > 1:
	f_name = sys.argv[1]
else:
	f_name = "A.in"

fh = open(f_name)
N = int(fh.readline())

def left(i):
	return 2*i+1
def right(i):
	return 2*i+2

def c_min_any(a, b):
	if a is None:
		return b
	if b is None:
		return a
	return min(a, b)

def c_min_all(a, b):
	if a is None:
		return None
	if b is None:
		return None
	return a + b

def c_min_add(a, b):
	if a is None:
		if b is None:
			return b
		return b+1
	if b is None:
		return a
	return min(a, b+1)

def calc_min(nodes, v):
	M	= len(nodes)
	changes_0	= [None] * M
	changes_1	= [None] * M
	MI	= (M-1) / 2
	for i in xrange(MI, MI + (M+1)/2):
		G, V = nodes[i]
		if V == 0:
			changes_0[i] = 0
		else:
			changes_1[i] = 0

#	import pdb; pdb.set_trace()

	for i in reversed(xrange((M-1)/2)):
		G, C = nodes[i]
		l, r = left(i), right(i)

		any_0 = c_min_any(changes_0[l], changes_0[r])
		all_0 = c_min_all(changes_0[l], changes_0[r])
		any_1 = c_min_any(changes_1[l], changes_1[r])
		all_1 = c_min_all(changes_1[l], changes_1[r])

		if G == OR:
			changes_0[i] = all_0
			changes_1[i] = any_1
			if C:
				changes_0[i] = c_min_add(changes_0[i], any_0)
		else:
			changes_0[i] = any_0
			changes_1[i] = all_1
			if C:
				changes_1[i] = c_min_add(changes_1[i], any_1)
#	print changes_0
#	print changes_1
	if v:
		r = changes_1[0]
	else:
		r = changes_0[0]
	if r is None:
		r = "IMPOSSIBLE"
	return r

for i in xrange(N):
	M, v = [int(x) for x in fh.readline().split()]
#	print "Mv", M, v
	nodes	= []
	for j in xrange((M-1)/2):
		G, C = [int(x) for x in fh.readline().split()]
		nodes.append((G, C))
	for j in xrange((M+1)/2):
		I = int(fh.readline())
		nodes.append((L, I))


	print "Case #%d: %s" % (i+1, calc_min(nodes, v))

