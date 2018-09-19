def search(root, node, graph):
	global visited
	for g in graph:
		if g[0] == node:
			visited.append((root, g[1]))
			search(root, g[1], graph)
		else:
			continue
		
	
with file('A-small-attempt0.in.txt') as f:
	out = file('out.txt','w')
	T = int(f.readline().strip())
	for t in xrange(1, T+1):
		N = int(f.readline().strip())
		graph = []
		for n in xrange(1,N+1):
			nums = map(int, f.readline().strip().split())
			nums.pop(0)
			for x in nums:
				graph.append([x,n])
		
		visited = []
		for x in xrange(1, N+1):
			search(x, x, graph)
		s=''
		if len(visited) != len(set(visited)):
			s = 'Yes'
		else:
			s = 'No'
		out.write('Case #%i: %s\n'%(t, s))
	out.close()