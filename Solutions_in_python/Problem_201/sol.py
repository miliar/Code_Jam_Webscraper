
import os
import sys
import math
import bisect

def next_midpoint(token_pairs):
	lefts = []
	rights = []
	maxes = []
	mins = []
	midpoints = []
	for pair in token_pairs:
		midpoint = math.floor( (pair[1] - pair[0])  / 2) + pair[0]

		midpoints.append(midpoint)

		ll =  abs(midpoint - pair[0]-1) 
		rr = abs(pair[1]-midpoint-1)
		lefts.append( ll )
		rights.append( rr )
		maxes.append( max(ll, rr) ) 
		mins.append( min(ll, rr) )


	matches = []
	mm = max(mins)
	for x in range(len(mins)):
		# print(midpoints[x])
		if mins[x] == mm and token_pairs[x][1]-token_pairs[x][0]>1:# and midpoints[x] not in list(map(lambda tt: tt[0], token_pairs)):
			matches.append(x)

	# print(midpoints)
	# print(mins)
	# print(maxes)

	if len(matches) == 1:
		finalidx = matches[0]
	else:
		maxlr = maxes[matches[0]]
		maxidx = matches[0]
		for match in matches:
			if maxlr < maxes[match]:
				maxlr = maxes[match]
				maxidx = match

		finalidx = maxidx#maxes.index(maxlr)
		# print("finalidx: %d" % finalidx)

	return ( (token_pairs[finalidx][0], midpoints[finalidx]),  (midpoints[finalidx], token_pairs[finalidx][1]), finalidx)


def calc_l_r(n, k):

	if (k == n):
		return (0, 0)

	taken_pairs = [(0, n+1)]

	for i in range(k):
		(leftpair, rightpair, newidx)  = next_midpoint(taken_pairs)

		# print(newidx)
		del taken_pairs[newidx]
		taken_pairs.insert(newidx, rightpair)
		taken_pairs.insert(newidx, leftpair)

		# print(taken_pairs)
		if i == k-1:
			print("leftpair (%d,%d)" % leftpair)
			print("rightpair (%d,%d)" % rightpair)
			return (leftpair[1]-leftpair[0]-1, rightpair[1]-rightpair[0]-1)



f = open(sys.argv[1])
outf = open(sys.argv[1] + ".out", 'w')

t = int(f.readline())
#
for t_th in range(t):

	tmp = list(map(int, f.readline().strip().split()))
	n = tmp[0]
	k = tmp[1]
	# print(n, k)
	L_s, R_s = calc_l_r(n, k)
	mx = max(L_s, R_s)
	mn = min(L_s, R_s)

	res = "Case #%d: %d %d" % (t_th+1, mx, mn)

	print(res)

	if t_th < t-1:
		res = res + "\n"
	outf.write(res)
