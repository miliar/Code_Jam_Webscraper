def combinations(items, k, repetition=False):
    "Selects k items with or without repetition in all possible ways"
    if k == 0:
        yield ()
    else:
        d = 1 - int(repetition)
        for i, item in enumerate(items):
            for rest in combinations(items[i+d:], k-1, repetition):
                yield (item,) + rest


for case in range(int(input())):
    n, A, B, C, D, x0, y0, M = map(int, raw_input().split())
    X, Y = x0, y0
    coords = [(X, Y),]
    for i in range(n-1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        coords.append((X, Y))
    count = 0
    for (x1, y1), (x2, y2), (x3, y3) in combinations(coords, 3):
        if (x1+x2+x3)%3 == 0 and (y1+y2+y3)%3 == 0:
            count += 1
    answer = count
    print 'Case #%d: %s' % (case+1, answer)
