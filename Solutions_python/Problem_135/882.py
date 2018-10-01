T = int(raw_input())

for t in xrange(1, T + 1):
    ans = int(raw_input())
    for row in xrange(4):
        data = map(int, raw_input().split(" "))
        if row + 1 == ans:
            ans1row = data
    ans = int(raw_input())
    for row in xrange(4):
        data = map(int, raw_input().split(" "))
        if row + 1 == ans:
            ans2row = data

    count = 0
    count = sum(ans2row.count(i) for i in ans1row)

    if count >1:
        s = "Bad magician!"
    elif count ==0:
        s = "Volunteer cheated!"
    else:
        for i in ans1row:
            if ans2row.__contains__(i):
                s = i
                break
    print "Case #%d: %s" % (t, s)
