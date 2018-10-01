r'''
args = ' '.join([
	r'',
])
import os
import sys
#os.system(sys.executable + " %s %s"%(__file__, args))
os.system(r'C:\Python36-32\python' + " %s %s"%(__file__, args))
r'''

# import ctypes
# print(ctypes.cdll.test.test(8))
# raise

input = """\
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
""".splitlines(keepends=True)




import sys
output = sys.stdout
if 1:
	input = open(r'A-small-attempt0.in').readlines()
	input = open(r'A-large.in').readlines()
	output = open("A.out", "w")
	
input = iter(input)

import math
from collections import defaultdict

sys.setrecursionlimit(1500)
	
def solve(D,N,O):
	print(O)
	l = [(D-K)/S for K,S in O]
	print(l)
	t = max(l)
	return D/t
	
import time
# raise
caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	D,N = map(int, next(input).split())
	O = []
	for i in range(N):
		K,S = map(int, next(input).split())
		O += [(K,S)]
	t0 = time.time()
	#print(D,N)
	res = solve(D,N,O)
	print("Case #%d:"%case, res, file=output)
	print('Case', case, time.time()-t0)
	sys.stdout.flush()
#'''
