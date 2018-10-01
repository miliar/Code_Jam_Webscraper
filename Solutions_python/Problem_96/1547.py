# Google Code Jam 2012
# Pawel Przytula
# p.przytula@students.mimuw.edu.pl

# Input reading helpers

import sys
def readline():
	s = sys.stdin.readline()
	return s.strip()

def readints():
	return [int(x) for x in readline().split()]
	
# END helpers ---------


		
if __name__ == "__main__":
	t = readints()[0]
	for i in xrange(t):
		test = readints()
		s = test[1]
		p = test[2]
		scores = test[3:]
			
		def score_test(fun, count_surprise):
			global s
			def test(acc, (x, m)):
				global s
				if count_surprise:
					if s > 0:
						r = int(fun(x, m))
						s -= r
						acc += r
				else:
					acc += int(fun(x, m))
				return acc
			return test
		
		pscores = [(x / 3, x % 3) for x in scores]
		is_score_gte_p = lambda x, m: x + int(m >= 1) >= p
		result = reduce(score_test(is_score_gte_p, False), pscores, 0)
		pscores = filter(lambda (x, m): not is_score_gte_p(x, m), pscores)
		# surprising
		is_score_gte_p = lambda x, m: (m == 2 and x + 2 >= p) or (x + 1 >= p and x > 0)
		result = reduce(score_test(is_score_gte_p, True), pscores, result)
		print "Case #%s: %s" % (i + 1, result)






