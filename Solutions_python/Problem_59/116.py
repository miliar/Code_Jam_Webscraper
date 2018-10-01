def case (casenum):
    existing = set(['/'])
    N, M = map(int, raw_input().split())
    for i in range(N):
        path = raw_input()
        existing.add(path)

    count = 0
    for i in range(M):
        path = raw_input().split('/')[1:]
        dir = ''
        for el in path:
            dir += '/' + el
            if dir not in existing:
                count += 1
                existing.add(dir)

    print 'Case #%i: %i' % (casenum, count)

T = int(raw_input())
for i in range(1, T+1):
    case(i)
