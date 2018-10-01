import sys, math

def minutes(str):
    return int(str[0])*600 + int(str[1])*60 + int(str[3])*10 + int(str[4])

def table(t, da,ia, db,ib):
    v = times.get(t, None)
    if v == None:
	times[t] = (da,ia, db,ib)
    else:
	xda,xia, xdb,xib = v
	times[t] = (xda+da, xia+ia, xdb+db, xib+ib)

line = sys.stdin.readline().strip()
N=int(line)
n=0

while n < N:
    n += 1
    line = sys.stdin.readline().strip()
    T = int(line)
    line = sys.stdin.readline().strip()
    NA, NB = line.split()
    NA = int(NA)
    NB = int(NB)
    times = {}
    for a in range(NA):
	line = sys.stdin.readline().strip()
	dep, arr = line.split()
	td, ta = minutes(dep), minutes(arr)
	table(td,  1,0, 0,0)
	table(ta+T,0,0, 0,1)
    for b in range(NB):
        line = sys.stdin.readline().strip()
        dep, arr = line.split()
        td, ta = minutes(dep), minutes(arr)
        table(td,  0,0,  1,0)
	table(ta+T,0,1,  0,0)
    # solve
    A=0
    inA=0
    B=0
    inB=0
    ts = times.keys()
    ts.sort()
    for t in ts:
	da,ia, db,ib = times[t]
	if ia:
	    inA += ia
	if ib:
	    inB += ib
	if da:
	    missing = inA - da
	    if missing < 0:
		A += -missing
		inA = 0
	    else:
		inA -= da
        if db:
            missing = inB - db
            if missing < 0:
                B += -missing
                inB = 0
            else:
                inB -= db

    print "Case #%s: %s %s" % (n, A, B)

