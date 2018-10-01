import sys

def gcd(a,b):
    x = max(a,b)
    y = min(a,b)

    if y == 0:
        return x
    else:
        while y > 0:
            r = x % y
            x = y
            y = r
        return x


def time_left(t):
    d = t[1] - t[0]
    for k in xrange(1,len(t)):
        d = gcd(d, abs(t[k] - t[k-1]))

    r = t[0] % d
    if r == 0:
        return 0
    else:
        return d - r

def process_case(case_number, t):
    T = time_left(t)
    print "Case #%d: %d" % (case_number, T)
    


def main():
    nbCases = int(sys.stdin.readline())
    for k, line in enumerate(sys.stdin):
        numbers = map(int, line.split())
        N = numbers[0]
        t = numbers[1:N+1]
        process_case(k + 1, t)


if __name__ == "__main__":
    main()
