import sys

#code from http://code.activestate.com/recipes/52201/
class Memo:
	def __init__(self, fn):
		self.fn = fn
		self.memo = {}
	def __call__(self, *args):
		if not self.memo.has_key(args):
			self.memo[args] = self.fn(*args)
		return self.memo[args]

#oowwnn code
def numSequence(pattern, base):
	#print pattern, "|", base
	if len(pattern) > len(base):
		return 0
	elif len(pattern) == len(base):
		if pattern == base:
			return 1;
		else:
			return 0;
	elif len(pattern) == 1:
		return base.count(pattern)
	else:
		if pattern[0] == base[0]:
			complete = numSequence(pattern, base[1:])
			partial = numSequence(pattern[1:], base[1:])
			return complete + partial
		else:
			return numSequence(pattern, base[1:])

#for memoization
sys.setrecursionlimit(15000)

numSequence = Memo(numSequence)
		
input = sys.stdin

for i in range(0, int(input.readline())):
	print "Case #%d: %04d" % (i+1, numSequence("welcome to code jam", input.readline())%10000)
