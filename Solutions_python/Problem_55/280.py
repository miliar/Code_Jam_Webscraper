def ride(queue, pos, k):
	people = 0
	cur_pos = pos
	while True:
		if cur_pos == pos + len(queue) or people + queue[cur_pos % len(queue)] > k:
			break
		people += queue[cur_pos % len(queue)]
		cur_pos += 1
	return cur_pos % len(queue), people

def main():
    for i in xrange(int(raw_input())):
        R, k, N = map(int, raw_input().split(" "))
        g = map(int, raw_input().split(" "))
	assert len(g) == N
	
	assert all(gi <= k for gi in g)

	m = [ride(g, pos, k) for pos in xrange(len(g))]
	
	m2 = []
	for pos in xrange(len(g)):
		res = 0
		pos = 0
		for r in xrange(1000):
			pos, this_money = m[pos]
			res += this_money
		m2.append((pos, res))
	
	res = 0
	pos = 0
	for r in xrange(R//1000):
		pos, this_money = m2[pos]
		res += this_money
	for r in xrange(R%1000):
		pos, this_money = m[pos]
		res += this_money
	
	print "Case #%i: %i" % (i+1, res)

main()
