import  math
import heapq

class X:
	
	def size(self):
		return self.j - self.i + 1
	
	def __lt__(self, other):
		dsize = self.size() - other.size()
		if dsize == 0:
			return self.i < other.i
		return dsize > 0
	
	def __init__(self, i, j):
		self.i = i
		self.j = j
	
	def __str__(self):
		return str(self.i) + ' ' + str(self.j)

def solve(n, k):
	a = [ 0 ] * (n + 1)
	q = [ ]
	heapq.heapify(q)
	x = X(1, n)
	heapq.heappush(q, ((x.size(), x.i), x))
	idx = 1
	while len(q) > 0:
		x = heapq.heappop(q)[1]
		mid = (x.i + x.j) // 2
		a[mid] = idx
		if idx == k:
			return mid - x.i, x.j - mid
		idx += 1
		
		L = X(x.i, mid -1)
		R = X(mid + 1, x.j)
		#print str(x) + ': ' + str(L) + ' / ' + str(R)
		if L.size() > 0:
			heapq.heappush(q, ((-L.size(), L.i), L))
		if R.size() > 0:
			heapq.heappush(q, ((-R.size(), R.i), R))

f = open('input', 'r')
lines = f.readlines()
nt = int(lines[0])
for tc in range(1, nt + 1):
	nk = lines[tc].split(' ')
	n = int(nk[0])
	k = int(nk[1])
	l, r = solve(n, k)
	print 'Case #' + str(tc) + ': ' + str(max(l, r)) + ' ' + str(min(l, r)) 