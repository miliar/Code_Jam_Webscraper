T = input()

class Horse:
	def __init__(self, D, K, S):
		self.K = K
		self.S = S

		self.time = (D - K) / S

def solution(case, sol):
	print "Case #%d: %.6f" % (case, sol)

for t in xrange(1, T+1):
	#print "Case #%d: ", % t

	data = raw_input().split(' ')
	D, N = int(data[0]), int(data[1])

	horses = []
	for i in xrange(N):
		h_data = raw_input().split(' ')
		horses.append(Horse(D, float(h_data[0]), float(h_data[1])))

	maxtime = max([h.time for h in horses])
	solution(t, D / maxtime)