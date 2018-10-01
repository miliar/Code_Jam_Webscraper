import sys; _tokens = sys.stdin.read().split(); _next_token = -1
def next(): global _next_token; _next_token += 1; return _tokens[_next_token]

def testcase(id):
	n = int(next())
	nums = [int(next()) for i in xrange(n)]
	#print n, nums
	bestsol = [-1]
	def go(i, xur1, xur2, cur1, cur2):
		if i == n:
			if xur1 == xur2 and cur1 > 0 and cur2 > 0 and cur1 > bestsol[0]:
				bestsol[0] = cur1
		else:
			go(i+1, xur1 ^ nums[i], xur2, cur1 + nums[i], cur2)
			go(i+1, xur1, xur2 ^ nums[i], cur1, cur2 + nums[i])
	go(0, 0, 0, 0, 0)
	bestsol = bestsol[0]
	y = 'NO' if bestsol == -1 else bestsol
	print "Case #{0}: {1}".format(id, y)

ncases = int(next())
for i in xrange(ncases):
	testcase(i+1)
