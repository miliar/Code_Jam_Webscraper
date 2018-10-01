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
  m = int(tmp[1])

  dirs = {}
  for i in range(0, n):
    d = sys.stdin.readline().strip()
    dirs[d] = True
  mk = 0
  for i in range(0, m):
    d = sys.stdin.readline().strip()
    parts = d.split("/")[1:]
    c = ""
    for x in parts:
      c = c + "/" + x
      if not dirs.has_key(c):
        dirs[c] = True
        mk += 1

  sys.stdout.write("Case #%d: %d" % (caseNum, mk))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
