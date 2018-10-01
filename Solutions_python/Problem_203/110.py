from __future__ import print_function
import sys
from sys import stdin


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def ln(f=int):
	return list(map(f,stdin.readline().strip().split()))

T, = ln()
INF = float('inf')

for test in range(T):
	R,C = ln()
	pnts = []
	cccc = []
	rrrr = []
	for r in range(R):
		row, = ln(str)
		for c,ch in enumerate(row):
			if ch!="?":
				pnts.append((r,c,ch))
				cccc.append(c)
				rrrr.append(r)


	print ("Case #" + str(test+1) + ": ")
	lastrow=None
	for r in range(R):
		row=""
		for c in range(C):
			ll= [(rp,cp,ch) for (rp,cp,ch) in pnts if rp>=r]
			if len(ll)!=0:
				xxx = [(rp,cp,ch) for (rp,cp,ch) in ll if rp==min([rr for rr in rrrr if rr>=r])]
				x = [(rp,cp,ch) for (rp,cp,ch) in xxx if cp>=c]
				if len(x)!=0:
					row+=x[0][2]
				else:
					row+=xxx[-1][2]
			else:
				row = lastrow
				break
		lastrow = row


		print(row)




