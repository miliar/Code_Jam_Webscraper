
def solve():
    m, s = raw_input().split()
    ans = 0
    count = 0
    for i, c in enumerate(s):
        c = int(c)
        if c > 0 and i > count:
            ans += i - count
            count += i - count
        count += c
    return ans

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        print 'Case #%s: %s' % (i, solve())

if __name__ == '__main__':
    main()
