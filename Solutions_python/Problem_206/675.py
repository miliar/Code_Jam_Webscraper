data = iter(open("A-large.in").read().splitlines())
T = int(next(data))
for caseNum in range(1, T + 1):
    d,n = map(int, next(data).split())
    horses = []
    for _ in range(n):
        horses.append(map(int, next(data).split()))

    max_time = 0.0
    for ki, si in horses:
        di = d - ki
        ti = float(di)/si
        max_time = max(max_time, ti)


    ans = d/max_time
    print "Case #%d: %f" % (caseNum, ans)