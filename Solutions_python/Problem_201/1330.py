from sortedcontainers import SortedList

def solve(n, k):
	if k > 2*n/3:
		return 0, 0

	s = SortedList()
	s.add(n)

	for i in range(k - 1):
		maxL = s.pop()
		half = maxL / 2
		s.add(half)

		if maxL % 2 == 0:
			s.add(half - 1)
		else:
			s.add(half)


	maxL = s.pop()

	half = maxL / 2
	if maxL == 0:
		x = y = 0
	elif maxL % 2 == 0:
		x = half
		y = half - 1
	else:
		x = y = maxL / 2

	return(max(x, y), min(x, y))


t = int(raw_input())

for i in xrange(1, t + 1):
  	n, k = [int(s) for s in raw_input().split(" ")]
  	result = solve(n, k)
 	print "Case #{}: {} {}".format(i, result[0], result[1])
 