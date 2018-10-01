import sys

def generategraph(k, groups): # k = seats, groups = group sizes
	next = 0
	visited = []
	euros = []
	sum_ = sum(groups)
	while not next in visited:
		visited.append(next)
		k_ = k
		while k_ >= groups[next] and k-k_+groups[next]<=sum_:
			k_ -= groups[next]
			next = (next+1) % len(groups)
		euros.append(k-k_)
	
	idx = visited.index(next)
	return euros[:idx], euros[idx:]
	
 
def f(R, k, groups):   # R = rounds, k = seats, groups = group sizes
	initial_list, loop_list = generategraph(k, groups)
	#print initial_list, loop_list
	
	euro = 0

	for i in range(len(initial_list)):
		euro += initial_list[i]
		R -= 1
		if R == 0:
			return euro
	
	whole_loops = R / len(loop_list)
	euro += whole_loops * sum(loop_list)
	R = R % len(loop_list)
	if R == 0:
		return euro

	for i in range(len(loop_list)):
		euro += loop_list[i]
		R -= 1
		if R == 0:
			return euro
	
	raise Exception, "Never Reached!"
	
inf = open(sys.argv[1])
T = int(inf.readline())
for i in range(T):
	R, k, N = [int(x) for x in inf.readline().split()]
	groups = [int(x) for x in inf.readline().split()]
	result = f(R, k, groups)
	print "Case #%d: %d" % (i+1, result)
