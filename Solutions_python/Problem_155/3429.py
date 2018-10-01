import os, re, sys
import unittest

class Test(unittest.TestCase):
	def test_1(self):
		self.assertEqual(main(4, "11111"), 0)
	def test_2(self):
		self.assertEqual(main(1, "09"), 1)
	def test_3(self):
		self.assertEqual(main(5, "110011"), 2)
	def test_4(self):
		self.assertEqual(main(0, "1"), 0)
	def test_5(self):
		self.assertEqual(main(6, "2000001"), 4)

#tCase = sys.stdin.readline().split()
tCase = int(sys.stdin.readline())

def main(N, M):
	if N == 0:
		return N
	else:
		clap = int(M[0])
		friends = 0
		for i in xrange(1, N + 1):
			if int(M[i]) > 0:
				if (i <= clap):
					clap += int(M[i])
				else:
					friends += i - clap
					clap += friends + int(M[i])
			#print i, clap, friends
		return friends
		
 
if __name__ == '__main__':
	#unittest.main()
	for i in xrange(tCase):	
		#frase = [str(x) for x in sys.stdin.readline().split(' ')]	
		#print "Case #%d: %s" % (i + 1, main(frase[0]))
		
		##Numbers
		N,M = [str(x) for x in sys.stdin.readline().split(' ')]	
		print "Case #%d: %d" % (i + 1, main(int(N),M))