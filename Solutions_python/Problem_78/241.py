IN = open('input.txt', 'r')

T = int(IN.readline())

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b % a, a)

for ttt in xrange(1, T + 1):

    line = IN.readline().strip().split()

    N = int(line[0])
    Pd = int(line[1])
    Pg = int(line[2])

    print 'Case #{}:'.format(ttt),

    if Pg == 0 and Pd == 0:
        print 'Possible'
        continue

    if Pg == 0:
        print 'Broken'
        continue

    if Pg == 100 and Pd != 100:
        print 'Broken'
        continue

    if 100 / gcd(Pd, 100) <= N:
        print 'Possible'
    else:
        print 'Broken'
    
