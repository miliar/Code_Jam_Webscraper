from math import ceil
from math import log

T = int(raw_input())
for t in range(1, T+1):
    L, P, C = map(int, raw_input().split())
    X = [P]
    while True:
	x = int(ceil(X[-1]/(C+0.0)))
	if x>L:
	    X.append(x)
	else:
	    break
    #print X
    V = [L]
    while True:
	v = V[-1]*C
	if v<P:
	    V.append(v)
	else:
	    break
    #print V
    a = log(len(X), 2)
    b = log(len(V), 2)
    y = int(ceil(min(a, b)))

    print "Case #%d: %d" % (t, y)
