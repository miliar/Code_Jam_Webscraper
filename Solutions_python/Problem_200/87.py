import sys

toks = sys.stdin.read().split()
toks.reverse()

T = int(toks.pop())
for t in xrange(T):
    s = toks.pop()

    suffix_len = 0
    while s != '0':
        for i, (cur, next) in enumerate(zip(s, s[1:])):
            if int(cur) > int(next):
                suffix_len += len(s) - i - 1
                num = int(s[:i+1]) - 1
                s = str(num)
                break
        else:
            break

    r = (s + '9'*suffix_len).lstrip('0')
    print 'Case #{}: {}'.format(t + 1, r)
