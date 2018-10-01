import sys

def readInt():
	return int(sys.stdin.readline().strip())

def readInts():
	return list(map(int, sys.stdin.readline().strip().split(" ")))

def readLine():
	return list(sys.stdin.readline().strip().split(" "))

TC = readInt()

for c in xrange(TC):
    N = readInt()
    line = readInts();
    SX = 0
    m = line[0]
    s = 0
    for i in xrange(N):
        x = line[i]
        SX ^= x
        s += x
        if m > x:
            m = x
    if SX == 0:
        print "Case #" + str(c+1) + ": " + str(s-m)
    else:
        print "Case #" + str(c+1) + ": NO"