import sys, string, math, bisect
from collections import defaultdict

rl = lambda: sys.stdin.readline().strip()

def cost(N, stops):
	i=stops
	return i*N - i*(i-1)/2

for cs in xrange(1,int(rl())+1):
	n,m = [int(z) for z in rl().split()]
	exitstops = defaultdict(list)
	entries = []
	originalcost = 0

	for oe in xrange(m):
		on,off,p = [int(z) for z in rl().split()]
		#print on,off,p
		exitstops[off].append( (on, p) )
		entries.append( (on, p) )
		originalcost += cost(n, off-on) * p
	#print
	#print exitstops
	#print entries

	sortedexitstops = exitstops.keys()
	sortedexitstops.sort()
	entries.sort()

	mm = 10**11

	totalcost = 0

	for stop in sortedexitstops:
		gettingoff = exitstops[stop]

		for alighter in gettingoff:
			num_alighters = alighter[1]
			while(num_alighters > 0):
				#find most recent entrant:
				entrycardi = bisect.bisect_right(entries, (stop, mm) )-1
				entrycard = entries[entrycardi]

				entrystop = entrycard[0]
				numentrants=entrycard[1]

				num_alighting = min(num_alighters, numentrants)

				tripcost = cost(n, stop-entrystop) * num_alighting
				totalcost += tripcost
				#print "alighting {} passengers at {} with entrycard {} at cost {}".format(num_alighting, stop, entrystop, tripcost)

				entrycard = (entrycard[0], numentrants - num_alighting)
				num_alighters -= num_alighting

				entries[entrycardi] = entrycard

				if entrycard[1] == 0:
					entries.pop(entrycardi)

	#print "orig: {}, new: {}, total: {}".format(originalcost, totalcost, originalcost - totalcost)
	print "Case #{}: {}".format(cs, (originalcost - totalcost) % 1000002013)



