import sys

def solve(case):
    r = int(sys.stdin.readline())
    s1, s2  = None, None
    for i in (1,2,3,4):
        line = sys.stdin.readline().strip()
        if i == r:
            s1 = set(line.split())

    r = int(sys.stdin.readline())
    for i in (1,2,3,4):
        line = sys.stdin.readline().strip()
        if i == r:
            s2 = set(line.split())

    result = s1.intersection(s2)
    l = len(result)
    if l == 0:
        print 'Case #%d: Volunteer cheated!' %case
    elif l == 1:
        print 'Case #%d: %s' % (case, result.pop())
    else:
        print 'Case #%d: Bad magician!' % case


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for case in xrange(N):
        solve(case+1)
