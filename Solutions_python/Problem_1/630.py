
def cmpr(a,b):
	if(len(a[1]) == len(b[1])):
		if(a[1][0] > b[1][0]):
			return -1
		elif(a[1][0] < b[1][0]):
			return 1
		else:
			return 0
	else:
		return cmp(b[1],a[1])
no_of_cases = input()
for current_case in range(no_of_cases):
	n = input()
	server_names = {}
	for i in range(n):
		s = raw_input()
		server_names[s] = []
	q = input()
	qcount = 0
	for i in range(q):
		qcount += 1
		search_query = raw_input()
		server_names[search_query] += [qcount]
	server_nameswitch = 0
	flag = 0
	while(True):
		orders1 = server_names.items()
		for i in orders1:
			if(len(i[1]) == 0):
				flag = 1
				break
		if(flag ==1):
			print "Case #%d: %d"%(current_case+1,server_nameswitch)
			break
		else:
			orders1.sort(cmpr)
			newserver = {}
			for i in server_names.keys():
				newserver[i] = []
			if(len(orders1[0][1]) > 0):
				queueno = orders1[0][1][0]
				servername = orders1[0][0]
				for (server,calls) in server_names.items():
					l1 = len(calls)
					for i in range(l1):
						if(calls[i] >= queueno):
							newserver[server] += [calls[i]]
				server_names = newserver
				server_nameswitch += 1


