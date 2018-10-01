import sys

def istidy(x):
    s = str(x)
    t = 0
    for c in s:
        if t > int(c):
            return False
        t = int(c)
    return True

def solve(x):
    while not istidy(x):
        x = x - 1
    return x

T = int(sys.stdin.readline())
for _c in range(T):
    N = int(sys.stdin.readline())
    y = solve(N)
    print "Case #%d: %d" % (_c + 1, y)
