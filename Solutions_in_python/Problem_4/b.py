import sys

#parse tyd fokken self
def timeinminutes(tehtime):
	#get something like '08:45'
	tehtime = tehtime.split(':')
	minutes = int(tehtime[0])*60
	minutes += int(tehtime[1])
	return minutes

f = open(sys.argv[1], 'r')

N = int(f.readline())

for case in range(N):
	atrains = 0
	btrains = 0
	
	T = int(f.readline())
	tuple = f.readline().split(' ')
	NA = int(tuple[0])
	NB = int(tuple[1])

	a_arrivals = []
	a_departures = []
	for atrips in range(NA):
		line = f.readline().strip().split(' ')
		a_arrivals += [timeinminutes(line[1])]
		a_departures += [timeinminutes(line[0])]
	
	b_arrivals = []
	b_departures = []
	for btrips in range(NB):
		line = f.readline().strip().split(' ')
		b_arrivals += [timeinminutes(line[1])]
		b_departures += [timeinminutes(line[0])]

	a_departures.sort()
	a_arrivals.sort()
	
	b_departures.sort()
	b_arrivals.sort()

	needed_at_a = 0
	needed_at_b = 0

	#print 'a_departures = ', a_departures
	#print 'b_arrivals = ', b_arrivals

	#print 'b_departures = ', b_departures
	#print 'a_arrivals = ', a_arrivals
	

	for departure in a_departures:
		one_was_waiting = 0
		for arrival in b_arrivals:
			if (arrival + T <= departure) and (one_was_waiting == 0):
				b_arrivals.remove(arrival)
				one_was_waiting = 1
		if one_was_waiting == 0:
			needed_at_a += 1
			
	for departure in b_departures:
		one_was_waiting = 0
		for arrival in a_arrivals:
			if (arrival + T <= departure) and (one_was_waiting == 0):
				a_arrivals.remove(arrival)
				one_was_waiting = 1
		if one_was_waiting == 0:
			needed_at_b += 1
	
	print 'Case #%s: %s %s' %(case+1, needed_at_a, needed_at_b)