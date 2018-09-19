#!/usr/bin/python
'''
Google codejam template
'''
import sys
from pprint import pprint
#fh = sys.stdin
fh = open(sys.argv[1])
cases = int(fh.readline())

def trace(p):
	'''
	Starting at node P, mark all nodes which depend on it
	'''
	while True:
		if v[p]:
			return True
		v[p] = 1
		if len(inh[p]) == 0:
			return False
		if len(inh[p]) > 1:
			for i in inh[p]:
				#print 'p=%s, i=%s' % (p, i)
				if trace(i):
					return True
			return False
		p = inh[p][0]

for case in range(1, cases+1):
	print 'Case #%i:' % case,
	inh = [None]
	n = int(fh.readline())
	for i in range(n):
		sp = [ int(i) for i in fh.readline().split() ]
		assert sp[0] == len(sp) - 1
		del sp[0]
		inh.append(sp)

	#print 'inh:',
	#pprint(inh)
	diamond = False
	for i in range(1, n+1):
		v = [0] * (n+1)
		if trace(i):
			diamond = True
			break
	print 'Yes' if diamond else 'No'
	sys.stdout.flush()
