infile = open('freecell.in')
outfile = open('freecell.out', 'w')

T = int(infile.readline().strip())

def gcd(a, b):
    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    return gcd(b % a, a)

for t in xrange(T):
    N, PD, PG = [int(s) for s in infile.readline().strip().split()]
    print N, PD, PG
    if ((PG == 100 and PD < 100)
        or (PG == 0 and PD > 0)
        or 100 / gcd(PD, 100) > N):

        print 'broke'
        outfile.write('Case #%d: Broken\n' % (t + 1))
        continue
    outfile.write('Case #%d: Possible\n' % (t + 1))
