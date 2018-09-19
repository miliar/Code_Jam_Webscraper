import sys

def x(l):
    return reduce(lambda x,y:x^y, l)

def s(l):
    return reduce(lambda x,y:x+y, l)

ii = 0
for i in range(1, int(sys.stdin.readline())+1):
    line = sys.stdin.readline().rstrip().split()
    line = sys.stdin.readline().rstrip().split()
                    
    #print line
    ar = []
    for l in line: ar.append(int(l))
    ar = sorted(ar)
    mx = -1
    for i in range(1,len(ar)):
        if x(ar[:i]) == x(ar[i:]):
            if s(ar[i:]) > mx:
                mx = s(ar[i:])

    ii += 1
    if mx == -1:
        print "Case #%d: NO"%ii
    else:
        print "Case #%d: %s"%(ii, mx)
    