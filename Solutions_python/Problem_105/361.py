#!/usr/bin/python
# problem1.py (Diamond Inheritance)

class GoogleJam:
	""" Problem solving iterator """
	
	def __init__(self, inf='data.in', outf='data.out'):
		self.fin = open(inf, 'r')
		self.fout = open(outf, 'w')

		# Reads test cases
		self.T = int(self.fin.readline())
		self.index = 0	# Inits iterator

	def __iter__(self):
		return self

	def findp(self, node, fnode):
		if fnode != None:
			if node in self.vnode:
				for i in xrange(len(self.vnode)):
					if node == self.vnode[i]:
						pos = i
				if self.vfnode[pos] != fnode:
					return True
				else:
					return False
			else: 
				self.vnode.append(node)
				self.vfnode.append(fnode)
		
		for p in self.Paths[node-1]:
			if self.findp(p, node):
				return True
		else:
			return False

	def solve(self):
		""" Problem solving algorithm """
		#-----------------------------------------------------------------------
		N = self.N

		for i in xrange(N):
			self.vnode = []
			self.vfnode = []

			if self.findp(i, None):
				return True
		else:
			return False

		#-----------------------------------------------------------------------
		return None # Return the result for the current test case 

	def next(self):
		# Increment iterator
		if self.index >= self.T: raise StopIteration
		self.index += 1

		# Read test case data

		# For example:
		# self.N = int(self.fin.readline())
		# self.limits = [[int(w) for w in self.fin.readline().split()] for n in xrange(self.N)]

		#---------------------------------------------------------------------------
		self.N = int(self.fin.readline())
		self.Paths = [[int(w) for w in self.fin.readline().split()] for n in xrange(self.N)]
		self.Count = []
		
		for p in self.Paths:
			self.Count.append(p[0])
			p.pop(0)

		#---------------------------------------------------------------------------
		return self.solve() # Calls the solving algorithm for the currently read test case

	def __del__(self):
		self.fin.close()
		self.fout.close()

# Program entry point
problems = GoogleJam()

# Iterating the problems in the test cases
for p in problems:
	# Print result
	if p == True:
		problems.fout.write('Case #{0}: Yes\n'.format(problems.index))
	else:
		problems.fout.write('Case #{0}: No\n'.format(problems.index))
	# Debug print
	print 'Case #{0}: {1}'.format(problems.index, p)
