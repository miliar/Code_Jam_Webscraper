# make it global for memoization

A = None

class Memoize:
	def __init__ (self, f):
		self.f = f
		self.mem = {}
	def __call__ (self, *args):
		if args in self.mem:
			return self.mem[args]
		else:
			tmp = self.f(*args)
			self.mem[args] = tmp
			return tmp

def rec(i,g1,g2):
	if i == len(A):
		if g1 != 0 and g1 == g2:
			return 0
		return None
	
	w = rec(i+1,g1 ^ A[i], g2)
	if w is not None:
		w += A[i]
	
	v = rec(i+1,g1, g2 ^ A[i])
	return max(w,v)

def solve(a):
	global A
	X = 0
	for x in a:
		X ^= x

	if X != 0:
		return "NO"

	A = a
	v = rec(0,0,0)
	return "%d" % v

def gcj():
	f = open("data","r")
	T = int(f.readline())
	for i in range(1,T+1):
		# test case specifics
		f.readline() # N
		test_case = map(int, f.readline().strip().split(' ')) 
		sol = solve(test_case)
		print "Case #%d: %s" % (i, sol)
		# end test case specific
	f.close()

if __name__ == "__main__":
	gcj()





			
