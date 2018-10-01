import networkx as nx

t = input()

for case in xrange(1,t+1):
	g = nx.Graph()
	n,q = map(int, raw_input().split())
	hd=[];hs=[]
	for x in xrange(n):
		t1, t2 = map(int, raw_input().split())
		hd.append(t1)
		hs.append(t2)
	li = []
	for x in xrange(n):
		li.append(list(map(int, raw_input().split())))
	u, v = map(int, raw_input().split())
	dist = []
	for x in xrange(len(li)):
		if x!=n-1: 
			dist.append(li[x][x+1])
	#print dist
	for x in xrange(n-1):
		#print '!!!!!!!!!'
		y = x
		while True:
			y = y+1
			if y > n-1: break
			#print '********'
			#print hd[x]
			#print dist[y-1]
			if hd[x] >= dist[y-1]:
				#print '----'
				di = 0
				#print dist
				di = sum(dist[x:y])
				#print x, y, di
				g.add_edge(x, y, ti = (di*1.0/hs[x]))
				hd[x]-=dist[y-1]
			else:
				break
	#print nx.dijkstra_path(g, 0, n-1, 'ti')
	print "Case #%d: %.10f"%(case, nx.dijkstra_path_length(g, 0, n-1, 'ti'))
	#print nx.dijkstra_path_length(g, 0, n-1, 'ti')


	#print li

	#print "Case #%d: %d %d"%(case, max(t1, t2), min(t1, t2))




























