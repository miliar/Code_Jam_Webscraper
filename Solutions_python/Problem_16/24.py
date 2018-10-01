#!/usr/bin/python
# Google Code Jam 2008
# Problem 2-D
# zzmike

import sys
import re
from Numeric import *
#from decimal import *

# ---------------------------------------------------------------------------------------------------------------

sys.setcheckinterval(10000)
PI = arccos(-1)
PI_2 = arccos(-1) / 2

#getcontext().prec = 200
#getcontext().rounding = ROUND_DOWN

# ---------------------------------------------------------------------------------------------------------------

#
def permutate(seq):
	if not seq:
		return [seq]
	else:
		temp = []
	for k in range(len(seq)):
		part = seq[:k] + seq[k+1:]
		for m in permutate(part):
			temp.append(seq[k:k+1] + m)
	return temp



def solve(caseNum):
	k = int(sys.stdin.readline().strip())
	s = sys.stdin.readline().strip()

	best = len(s) + 100

	perm = permutate(range(k))
	for p in perm:
		last = "0"
		count = 0
		t = 0
		offset=0
		for i in range(0, len(s)):
			if s[p[i%k]  + offset ] != last:
				count += 1
				last = s[p[i%k] + offset]
			t += 1
			if t == k:
				offset += k
				t = 0 
			if count > best: break
		if count < best:
			best = count
			

	sys.stdout.write("Case #%d: %s" % (caseNum, best))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
