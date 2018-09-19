import math
import sys

def ispal(n):
    s = str(n)
    return s == s[::-1]

def ispalsq(n):
    sqrt = int(math.sqrt(n) + .01)
    if sqrt ** 2 != n:
        return False
    return ispal(n) and ispal(sqrt)

nums = set()
def search(s, l, idx):
    if l % 2 == 0:
        m = s + s[::-1]
    else:
        m = s[:-1] + s[::-1]
    assert ispal(m)
    n = int(m) ** 2
    if not ispal(n):
        # print m, False
        return 0
    # print m, int(m)**2

    nums.add(n)
    for i in xrange(idx, len(s)):
        s2 = list(s)
        s2[i] = str(int(s2[i])+1)
        s2 = ''.join(s2)
        search(s2, l, i)


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    for l in xrange(1, 75):
        search("1" + "0" * ((l-1)/2), l, 0)
    assert any(n > 10**120 for n in nums)

    t = int(f.readline())
    for _t in xrange(t):
        a, b = map(int, f.readline().split())

        total = len([n for n in nums if a <= n <= b])
        print "Case #%d: %d" % (_t+1, total)

