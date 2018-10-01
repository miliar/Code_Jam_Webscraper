# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import numpy as np
t = int(raw_input())  # read a line with a single integer
for j in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  usrs = [1,n+2]
  middles = [(usrs[i]+usrs[i+1])/2 for i in range(len(usrs)-1)]
  dist = [usrs[i+1]-usrs[i] for i in range(len(usrs)-1)]
  for usr in range(k):
	max_idx_dist = np.argmax(dist)
	usrs.append(middles[max_idx_dist])
	usrs = sorted(usrs)
	if usr == k-1:
		last_idx = usrs.index(middles[max_idx_dist])
		Ls = usrs[last_idx]-usrs[last_idx-1]-1
		Rs = usrs[last_idx+1]-usrs[last_idx]-1

	middles = [(usrs[i]+usrs[i+1])/2 for i in range(len(usrs)-1)]
  	dist = [usrs[i+1]-usrs[i] for i in range(len(usrs)-1)]
  print "Case #{}: {} {}".format(j,Rs, Ls)
  # check out .format's specification for more formatting options

