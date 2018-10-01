import sys

T = int(sys.stdin.readline())
for t in xrange(T):
    s, k = sys.stdin.readline().rstrip().split(' ')
    s = list(s)
    k = int(k)
    ret = 0
    for i in xrange(len(s) - k + 1):
        if s[i] == '-':
            for j in xrange(i, i + k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
            ret += 1
    if any(c == '-' for c in s):
        ret = 'IMPOSSIBLE'
    sys.stdout.write('Case #%d: %s\n' % (t + 1, ret))
