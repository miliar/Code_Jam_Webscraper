T = int(raw_input())

for case in range(1, T+1):
	N, M = map(int, raw_input().split())
	fileSys = set()
	numMkdirs = 0
	
	# Initials filesys
	fileSys.add('/')
	for i in range(N):
		path = raw_input().split('/')
		p = ''
		for j in range(len(path)):
			p = p + '/' + path[j]
			fileSys.add(p)
	
	# New dirs
	for i in range(M):
		path = raw_input().split('/')
		p = ''
		for j in range(len(path)):
			p = p + '/' + path[j]
			if p not in fileSys:
				fileSys.add(p)
				numMkdirs += 1
	
	print 'Case #' + str(case) + ': ' + str(numMkdirs)

