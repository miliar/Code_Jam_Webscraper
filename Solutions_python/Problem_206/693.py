def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                D,N = parseTuple(f)
                print D,N
                horses = []
                for i in range(N):
                    Ki,Si = parseTuple(f)
                    horses.append((Ki,Si))

                x = solve(D,horses)
                print>>g, 'Case #%d: %f'  % (n+1,x)
                print 'Case #%d: %f'  % (n+1,x  )


import sys, itertools
def solve(D,horses):
    timeToD = max(float(D-K)/S for K,S in horses)
    return float(D)/timeToD



if __name__ == '__main__':
    main('A-test.in', 'A-test.out')
    #main('A-small-attempt0.in', 'A-small-attempt0.out')
    main('A-large.in', 'A-large.out')
    sys.exit(0)


