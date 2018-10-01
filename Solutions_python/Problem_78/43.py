
def gcd(x, y):
    while x:
        x, y = y % x, x
    return y

def solve(data):
    N, PD, PG = data

    gcdD = gcd(PD, 100)
    WD, D = PD/gcdD, 100/gcdD

    if D > N:
        return 'Broken'
    elif PD != PG and PG in (0, 100):
        return 'Broken'
    else:
        return 'Possible'


def get_input():
    return map(int, raw_input().split())

def main():
    T = int(raw_input())
    for i in xrange(T):
        print 'Case #%d: %s' % (i + 1, solve(get_input()))

if __name__ == '__main__':
    main()
