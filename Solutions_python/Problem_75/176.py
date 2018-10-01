def reduce(bag):
	l = len(bag)
	pair = set(bag[-2:])
#	print pair
	reductions = [prod for prod in prods if pair == prod[0]]
	if reductions:
#		print reductions
		del bag[-2:]
		bag.append(reductions[0][1])
	return bag
		
def collapse(bag):
	if len(bag) <= 1:
		return bag
	last = bag[-1]
	for opp in opps:
		if opp.intersection(bag) == opp:
			return []
	return bag
			

def solve(series):
	bag = []
	for c in series:
		bag.append(c)
		if len(bag) > 1:
			bag = reduce(bag)
			bag = collapse(bag)
	return bag

T = int(raw_input())
for case in xrange(1, T + 1):
	line = raw_input().split()
	index = 0
	C = int(line[index])
#	print "C is %d" % C
#	print line[index + 1: index + 1 + C]
	prods = [(set([s[0], s[1]]), s[2]) for s in line[index + 1: index + 1 + C]]
	index = C + 1
	D = int(line[index])
#	print "D is %d" % D
#	print line[index + 1: index + 1 + D]
	opps = [set([s[0], s[1]]) for s in line[index + 1: index + 1 + D]]
	index = C + D + 2
	N = int(line[index])
	series = line[index + 1]
	ans = solve(series)
#	print "Productions: %s" % prod
#	print "Opposites: %s" % opp
#	print "Series: %s" % series
	print "Case #%d: [%s]" % (case, ", ".join(ans))

	