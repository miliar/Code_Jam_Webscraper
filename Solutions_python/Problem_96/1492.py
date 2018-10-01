if __name__ == '__main__':
    import sys

    T = int(sys.stdin.readline())

    for i in xrange(T):
        line = sys.stdin.readline().strip().split(" ")
        N, S, p = line[:3]
        googlers = line[3:]

        N = int(N)
        S = int(S)
        p = int(p)

        score = 0

        if p <= 0:
            score = N
        else:
            for googler in googlers:
                if not int(googler):
                    continue

                if (int(googler))/2. < p:
                    continue

                tmp = p - (int(googler) - p)/2.

                if tmp <= 2. and tmp > 1. and S > 0:
                    score += 1
                    S -= 1
                elif tmp <= 1.:
                    score += 1

        print "Case #%d: %d" % (i+1, score)
