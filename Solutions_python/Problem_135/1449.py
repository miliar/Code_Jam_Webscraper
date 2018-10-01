t = int(raw_input())
case = 0
while t > 0:
    t -= 1
    case += 1
    r1 = int(raw_input())
    a = []
    for _ in xrange(4):
        a.append(map(int, raw_input().split()))

    r2 = int(raw_input())
    b = []
    for _ in xrange(4):
        b.append(map(int, raw_input().split()))

    sa = set(a[r1-1])
    sb = set(b[r2-1])
    intersection = sa.intersection(sb)
    kase = 'Case #%s: ' % case
    if len(intersection) == 1:
        print kase, intersection.pop()
    elif len(intersection) > 1:
        print kase, 'Bad magician!'
    else:
        print  kase, 'Volunteer cheated!'
