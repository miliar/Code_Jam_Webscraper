import sys
import string
def getline():
	return sys.stdin.readline()[:-1]
vendor = []
place = []
dist = []
sum_vendor = []
cluster = {}
def work_cluster(u, v):
	offset = []
	head_offset = 0
	place_offset = 0
	d = dist[0]
	for i in range(u, v):
		place_offset = place[i] - place[u]
		offset.append(head_offset * d - place_offset)
		head_offset += vendor[i] - 1
		offset.append(head_offset * d - place_offset)
		head_offset += 1
	x = -0.5 * (min(offset) + max(offset))
	y = 0.5 * (max(offset) - min(offset))
	# print 'cluster[{0},{1}): {2},{4}, offset={3}'.format(u, v, x, offset, y)
	return x, y
def can_link(u, v, w):
	if cluster[(u,v)][0] + (sum_vendor[v] - sum_vendor[u]) * dist[0] + place[u] <= cluster[(v,w)][0] + place[v]:
		return True
	return False
def test_case():
	args = getline().split(' ')
	c = int(args[0])
	dist[:]=[]
	dist.append(float(args[1]))
	vendor[:]=[]
	sum_vendor[:]=[0]
	place[:]=[]
	for i in range(c):
		args = getline().split(' ')
		place.append(int(args[0]))
		vendor.append(int(args[1]))
		sum_vendor.append(sum_vendor[-1]+vendor[-1])
	#print sum_vendor
	cluster.clear()
	for i in range(c):
		for j in range(i, c):
			cluster[(i,j+1)] = (work_cluster(i, j+1))
	if c == 1:
		return cluster[(0, 1)][1]
	f = {}
	for k in range(1, c+1):
		f[(0, k)] = cluster[(0,k)][1]
		#print 'f({0},{1})={2}'.format(0, k, f[(0,k)])
		for j in range(1, k):
			if not can_link(0, j, k):
				#print 'cannot link (0,{0},{1})'.format(j,k)
				continue
			f[(j,k)] = max(cluster[(0,j)][1], cluster[(j,k)][1])
			for i in range(j):
				if not can_link(i, j, k) or not (i,j) in f:
					continue
				candidate = max(f[(i,j)], cluster[(j,k)][1])
				if candidate < f[(j,k)]:
					f[(j,k)] = candidate
			#print 'f({0},{1})={2}'.format(j, k, f[(j,k)])
	result = f[(0,c)]
	for i in range(1,c):
		if (i,c) in f and f[(i,c)] < result:
			result = f[(i,c)]
	return result

t = int(getline())
for i in range(t):
	print 'Case #{0}: {1}'.format(i+1, test_case())

