#debug 
def pr(*a):
	#return
	for x in a: print x,
	print
	
def split(size, left):
	mid = left + (size-1)//2
	leftSize = mid-left
	rightSize = size - leftSize - 1
	ret = []
	if leftSize > 0:
		ret.append((-leftSize, left))
	if rightSize > 0:
		ret.append((-rightSize, mid+1))
	return ret

def solve(n, k):
	que = Queue.PriorityQueue() # element (-size, leftIndex)
	que.put((-n, 0))
	for i in range(k-1):
		size, left = que.get()
		size = -size
		splits = split(size, left)
		for segment in splits:
			que.put(segment)

	size, left = que.get()
	size = -size
	if size % 2 == 0:
		return "%d %d"%(size/2, size/2 - 1)
	else:
		return "%d %d"%(size//2, size//2)
	
import sys, Queue
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, K = f.readline().strip().split()
	N, K = int(N), int(K)
	rt = solve(N, K)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()