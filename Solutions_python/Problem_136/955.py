import sys

rdLn = sys.stdin.readline

def readInt():
    return int(rdLn()[:-1])

def readNums():
    return map(float,(rdLn()[:-1]).split(' '))

T = readInt()

for i in range(1, T+1):
    [C,F,X] = readNums()

    t0 = 0
    r0 = 2
    t1 = C / r0
    r1 = r0 + F
    t2 = t1 + C / (r1 - r0)
    eq = (t2 - t1) * r1

    while (eq < X):
        t0 = t1
        r0 = r1
        t1 = t0 + C / r0
        r1 = r0 + F
        t2 = t1 + C / (r1 - r0)
        eq = (t2 - t1) * r1

    ans = t0 + X / r0

    print "Case #{0}: {1}".format(i,ans)
