
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    input = map(int, raw_input().split(' '))
    N = input[0]
    t = input[1:]
    d = [abs(t[i] - t[i + 1]) for i in xrange(N - 1)]

    magic = reduce(gcd, d)
    extra = (t[0] % magic)
    return magic - extra if extra else 0

def main():
    C = int(raw_input())
    for i in xrange(C):
        print 'Case #%d: %s' % (i + 1, solve())

if __name__ == '__main__':
    main()