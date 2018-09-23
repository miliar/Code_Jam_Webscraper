from queue import PriorityQueue as pqueue
class space:
	def __init__(self, number):
		self.number = number
	def __lt__(self, other):
		return self.number > other.number
	def __eq__(self, other):
		return self.number == other.number

def solve(N, K):
	pq = pqueue()
	pq.put(space(N))
	for i in range(K-1):
		n = pq.get().number-1
		pq.put(space(int(n/2)))
		pq.put(space(int(n/2)+n%2))
	last = pq.get().number-1
	return int(last/2), int(last/2)+last%2

def solve2(N, K):
	if K == 1:
		return solve(N, K)
	originK = K
	remainder = 0
	dis = 1
	while K > dis:
		# print("K:{0}	N:{1}	dis:{2}	remainder{3}	originK-K+N*dis+remainder={4}".format(K, N, dis, remainder, originK-K+N*dis+remainder))
		N -= 1
		remainder += (N % 2)*dis
		N = int(N / 2)
		K -= dis
		dis *= 2
	# print("K:{0}	N:{1}	dis:{2}	remainder{3}	originK-K+N*dis+remainder={4}".format(K, N, dis, remainder, originK-K+N*dis+remainder))
	if N == 0:
		res = 0
		remainder = 0
		last_remainder = 0
	else:
		res = int((N-1)/2)
		last_remainder = (N-1)%2
	# print("K:{0}	N:{1}	dis:{2}	remainder{3}	res:{4}".format(K, N, dis, remainder, res))
	if remainder >= K:
		if last_remainder == 1:
			return res+1, res+1
		else:
			return res, res+1
	elif last_remainder == 1:
		return res, res+1
	else:
		return res, res

def test():
	b = False
	for N in range(1, 1000):
		if N % 100 == 0:
			print(N)
		if b:
			break
		for K in range(1, N+1):
			if solve(N, K) != solve2(N, K):
				print(N, K)
				b = True
				break
	print("complete")

if __name__ == '__main__':
	# test()
	tc = int(input())
	for tcidx in range(1, tc+1):
		N, K = map(int, input().strip().split())
		# minv, maxv = solve(N, K)
		# print("Case #{0}: {1} {2}".format(tcidx, maxv, minv))
		minv, maxv = solve2(N, K)
		print("Case #{0}: {1} {2}".format(tcidx, maxv, minv))
