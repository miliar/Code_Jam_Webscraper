import sys
import math

def dist(start, end):
    if end > start:
        return end - start
    else:
        return 1440 - (start - end)

def solve_simple(C, J):
    Cs = len(C)
    Js = len(J)

    if Cs > 2 or Js > 2 or Cs + Js > 2:
        return 'DK'

    if Cs == 2:
        if min(dist(C[0][0], C[1][1]), dist(C[1][0], C[0][1])) <= 720:
            return 2
        else:
            return 4
    if Js == 2:
        if min(dist(J[0][0], J[1][1]), dist(J[1][0], J[0][1])) <= 720:
            return 2
        else:
            return 4
    if Cs == 1 and Js == 0:
        return 2
    if Cs == 0 and Js == 1:
        return 2
    if Cs == 1 and Js == 1:
        return 2


def solve(Cs, Js):

    Cs = sorted(Cs)
    Js = sorted(Js)

    return solve_simple(Cs, Js)

def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        Ac, Aj = map(int, sys.stdin.readline().split())
        Cs, Js = [], []
        for j in xrange(Ac):
            Cj, Dj = map(int, sys.stdin.readline().split())
            Cs.append((Cj, Dj))
        for j in xrange(Aj):
            Jj, Kj = map(int, sys.stdin.readline().split())
            Js.append((Jj, Kj))
        ans = solve(Cs, Js)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
