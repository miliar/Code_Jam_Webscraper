import sys

def one():
    t = int(sys.stdin.readline().strip())
    for times in xrange(0,t):
        n = int(sys.stdin.readline().strip())
        wires = []
        out = "Case #"+str(times+1)+":"
        for i in xrange(0,n):
            wires.append(map(int,sys.stdin.readline().strip().split()))
        count = 0
        for wire in wires:
            for comp in wires:
                d1 = wire[0] - comp[0]
                d2 = wire[1] - comp[1]
                if d1 < 0 and d2 > 0:
                    count += 1
                elif d1 > 0 and d2 < 0:
                    count += 1
        print out,count/2
one()

