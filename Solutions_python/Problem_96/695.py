import sys

def pack(x, p, surp):
    avg = x / 3
    rem = x % 3

    if x == 0 and p > 0:
        return False
    if p <= avg:
        return True

    if rem == 0:
        return (p - avg == 1) and surp
    if rem == 1:
        return (p - avg == 1)
    if rem == 2:
        if surp:
            return (p - avg <= 2)
        else:
            return (p - avg == 1)

def solve(N, S, p, t):
    count = 0

    for x in t:
        if pack(x, p, False):
            count += 1
        elif S > 0 and pack(x, p, True):
            S -= 1
            count += 1

    return count

def output(N, ans):
    print 'Case #{0}: {1}'.format(N, ans)

def main(fname):
    with open(fname, 'r') as f:
        N = int(f.readline())

        for i in xrange(N):
            a = [int(x) for x in f.readline().split(' ')]
            output(i + 1, solve(a[0], a[1], a[2], a[3:]))

if __name__ == '__main__':
    main(sys.argv[1]) 
