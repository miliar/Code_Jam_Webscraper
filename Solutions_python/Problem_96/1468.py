from math import ceil

T = int(raw_input())
for t in range(1, T+1):
    points = map(int, raw_input().split())
    S = points[1]
    p = points[2]
    points = points[3:]
    n = 0
    toInc = 0
    for i in points:
	m = ceil(i/3.0)
	if (m >= p):
	    n += 1
	elif ((i >= 2) and (i <= 27) and (i%3 != 1) and (m == p-1)):
	    toInc += 1
    n += min(S, toInc)
    print "Case #%d: %d" %(t, n)
