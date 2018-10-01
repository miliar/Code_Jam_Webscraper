from sys import stdin

def solve(n, l):
    ret = 0
    for i in range(n):
        if i+1-l[i]:
            ret += 1
    return ret

buf = []
for line in stdin:
    buf.insert(0, line)
N = int(buf.pop())
for i in range(1, N+1):
    print 'Case #%d: %#f' % (i, solve(int(buf.pop()), [int(e) for e in buf.pop().strip().split()]))
