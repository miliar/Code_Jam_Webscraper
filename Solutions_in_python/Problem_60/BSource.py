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


def solve(caseNum):
  tmp = sys.stdin.readline().strip().split(" ")
  n = int(tmp[0])
  k = int(tmp[1])
  b = int(tmp[2])
  t = int(tmp[3])

  xs = map(float, sys.stdin.readline().strip().split(" "))
  vs  = map(float, sys.stdin.readline().strip().split(" "))

  ts = []
  for i in range(0, n):
    ts.append(((b - xs[i]) / vs[i] <= t))

  swaps = 0
  end = 0
  ts.reverse()
  while(end < k):
    # Search first true
    if ts.count(True) == 0:
      sys.stdout.write("Case #%d: IMPOSSIBLE" % (caseNum))
      return
    i = ts.index(True)
    swaps += i
    ts.remove(True)
    end += 1

  sys.stdout.write("Case #%d: %d" % (caseNum, swaps))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
