import sys
import re
from Numeric import *

# ---------------------------------------------------------------------------------------------------------------

sys.setcheckinterval(10000)
PI = arccos(-1)
PI_2 = arccos(-1) / 2

# ---------------------------------------------------------------------------------------------------------------
# Global variables
#src_table = array(zeros(256), Int)

# ---------------------------------------------------------------------------------------------------------------

def solve(caseNum):
	S = int(sys.stdin.readline().strip())
	eng = {}
	for i in range(0, S):
		eng[sys.stdin.readline().strip()] = i

	Q = int(sys.stdin.readline().strip())
	c = S
	ch = 0

	v = [True] * S
	for i in range(0, Q):
		s = sys.stdin.readline().strip()
		idx = eng[s]
		if v[idx]:
			v[idx] = False
			c -= 1

		if c == 0:
			ch += 1
			for j in range(0,S):
				v[j] = True
				c = S - 1
			v[idx] = False


	sys.stdout.write("Case #%d: %d" % (caseNum, ch))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
