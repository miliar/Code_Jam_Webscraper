import math

def find(n, k):
	stalls = {n:1}
	keys = [n]
	maxd = n
	mind = n
	while k > 0:
		curmax = max(keys)
		maxd = int(math.ceil((curmax-1)/2.0))
		mind = int(math.floor((curmax-1)/2.0))
		if stalls[curmax] > 1:
			stalls[curmax] = stalls[curmax]-1
		else:
			stalls.pop(curmax)
			keys.remove(curmax)
		if maxd in keys:
			stalls[maxd] = stalls[maxd]+1
		else:
			keys.append(maxd)
			stalls[maxd] = 1
		if mind in keys:
			stalls[mind] = stalls[mind]+1
		else:
			keys.append(mind)
			stalls[mind] = 1
		k = k - 1

	return maxd, mind


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this 
  maxd, mind = find(n, k)
  print "Case #{}: {} {}".format(i, maxd, mind)
  # check out .format's specification for more formatting options

