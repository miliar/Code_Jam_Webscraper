import math
import sys

def solve(P):
    P.sort(reverse=True)
    minutes = P[0]
    for normal in xrange(1, P[0] + 1):
        special = sum(
            int(math.ceil(1.0 * p / normal)) - 1 if p > normal else 0
            for p in P
        )
        minutes = min([special + normal, minutes])
    return minutes

def main():
    inp = iter(sys.stdin)
    T = int(next(inp))
    x = 1
    problems = 0
    while x <= T:
        D = int(next(inp), 10)
        P = [int(i, 10) for i in next(inp).split(" ", D)]
        print "Case #{0}: {1}".format(x, solve(P))
        x += 1

if __name__ == "__main__":
    main()
