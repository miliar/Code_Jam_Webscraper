import sys
f = open(sys.argv[1])
cases = int(f.readline())
def nums(f):
    return [int(x) for x in f.readline().split()] 
for case in range(1,cases+1):
    answer = 0
    N = int(f.readline())
    L = []
    for i in range(N):
        Ai, Bi = nums(f)
        for Aj, Bj in L:
            if (Ai < Aj and Bi > Bj) or (Ai > Aj and Bi < Bj):
                answer += 1
        L.append((Ai,Bi))
    print "Case #%d: %d" % (case, answer)

        


