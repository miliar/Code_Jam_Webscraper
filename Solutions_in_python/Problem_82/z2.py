import sys
from array import array

def readInt():
	return int(sys.stdin.readline().strip())

def readInts():
	return list(map(int, sys.stdin.readline().strip().split(" ")))

def readLine():
	return list(sys.stdin.readline().strip().split(" "))

def readChars():
	return list(sys.stdin.readline().strip())

T = readInt()
for tc in xrange(T):
    (C, D) = readInts()

    A = []
    for i in xrange(C):
        A.append(readInts())
    #print A

    mx = 0
    for i in xrange(C):
        j = i
        v = 0 #A[i][1]
        while (j < C):
            v += A[j][1]
            dst = A[j][0] - A[i][0]
            ndst = (v-1) * D
            #print 'n' + str(ndst) + ' d' + str(dst) + ' v' + str(v)
            if (mx < ndst-dst):
                mx = ndst-dst
            j += 1

    print "Case #" + str(tc+1) + ": " + str(mx/2.0)
