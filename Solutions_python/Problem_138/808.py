import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >=2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    no_cases = int(f.readline())
    for case in xrange(no_cases):
        no_wt = int(f.readline())
        n = naomi = sorted([float(i) for i in f.readline().split()], reverse=True)
        k = ken = sorted([float(i) for i in f.readline().split()], reverse=True)
        i = 0
        win = 0
        nw = no_wt
        while i < nw:
            if naomi[-1] > ken[-1]:
                naomi = naomi[:-1]
                ken = ken[:-1]
                win += 1
            elif naomi[-1] < ken[0]:
                naomi = naomi[:-1]
                ken = ken[1:]
            i += 1
        dwar = 0
        for i in range(no_wt):
            if n[i] > k[i]:
                dwar += 1
        dwar = max(len(naomi) + win, dwar)
        war = 0
        naomi = n
        ken = k
        nw = no_wt
        for wt in naomi:
            if wt > ken[0]:
                ken = ken[:-1]
                nw -= 1
                war += 1
            elif ken[-1] > wt:
                ken = ken[:-1]
                nw -= 1
            else:
                for i in range(nw - 1):
                    if ken[i] > wt and wt >= ken[i + 1]:
                        ken = ken[:i] + ken[i + 1:]
                        nw -= 1
        print "Case #%d: %d %d" % (case + 1, dwar, war)