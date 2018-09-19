import sys

EPS = 1e-8

def solve(C, F, X):
    def do_solve(f):

        if f*EPS > X:
            return 0.0
        return min(X/f, C/f + do_solve(f + F))

    if X < C:
        return X/2.0
    
    t = 0.0
    f = 2.0
    answer = X / f
    while (t < answer and f*EPS < X):
        answer = min(answer, t + X / f)
        t+= C / f
        f+= F

    return answer


def main():
    T = int(sys.stdin.readline())
    for k in xrange(T):
        C, F, X = map(float, sys.stdin.readline().split())
        answer = solve(C, F, X)
        print "Case #{0}: {1:.7f}".format(1 + k, answer)
        

if __name__ == '__main__':
    main()
