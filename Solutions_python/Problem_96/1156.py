#!/usr/bin/python

def solve(S, P, results):
    counter = 0
    for result in results:
        base = result / 3
        supp = result % 3
        if base >= P:
            counter += 1
        elif P - base == 2 and supp == 2 and S > 0:
            S -= 1
            counter += 1
        elif P - base > 2:
            pass
        elif P - base == 1 and supp >= 1:
            counter += 1
        elif P - base == 1 and supp == 0 and S > 0 and base:
            S -= 1
            counter += 1
    return counter

def main():
    T = int(raw_input())
    for testid in xrange(1, T+1):
        line = raw_input().split()
        N = int(line[0])
        S = int(line[1])
        P = int(line[2])
        results = map(int, line[3:])
        print 'Case #%s: %s' % (testid, solve(S, P, results))

if __name__ == "__main__":
    main()