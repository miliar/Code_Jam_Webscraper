import sys

def readInt():
	return int(sys.stdin.readline().strip())

def readInts():
	return list(map(int, sys.stdin.readline().strip().split(" ")))

def readLine():
	return list(sys.stdin.readline().strip().split(" "))

TC = readInt()

for c in xrange(TC):
    ROBOTS = {
        'O' : { 'ts' : 0, 'pos' : 1 },
        'B' : { 'ts' : 0, 'pos' : 1 }
    }
    TS = 0
    L = readLine()
    n = 2 * int(L.pop(0))
    for i in xrange(n):
        if (i & 1 == 0):
            R = ROBOTS[L[i]]
        else:
            walk = abs(int(L[i]) - R['pos'])
            midwork = TS - R['ts']
            if midwork >= walk:
                TS += 1
            else:
                TS += 1 + (walk - midwork)
            R['ts'] = TS
            R['pos'] = int(L[i])
    print "Case #"+str(c+1)+": "+str(TS)