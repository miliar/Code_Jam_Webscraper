def put(ls, isLast):
    totMin = 0
    minr = 0
    maxr = 0
    index = 0
    for i in xrange(len(ls)):
        (l, r) = ls[i]
        _min = l if l < r else r
        _max = l if l > r else r
        if _min > totMin:
            index = i
            minr = _min
            maxr = _max
            totMin = _min
        elif _min == totMin:
            minr = -1
            if _max > maxr:
                maxr = _max
                index = i

    if isLast:
        return ls[index]

    ls[index] = (-1, -1)

    for i in xrange(len(ls)):
        (l, r) = ls[i]
        if i == index:
            continue
        elif i < index:
            _r = index - i - 1
            if _r < r:
                ls[i] = (l, _r)
        else:
            _l = i - index - 1
            if _l < l:
                ls[i] = (_l, r)

    return ls


t = int(raw_input())
for i in xrange(1, t + 1):
    s, p = [int(x) for x in raw_input().split(" ")]

    ls = [(k, s - 1 - k) for k in xrange(s)]

    for _i in xrange(p):
        if _i == p-1:
            (l, r) = put(ls, True)
            _max = l if l > r else r
            _min = l if l < r else r

            _max = 0 if _max < 0 else _max
            _min = 0 if _min < 0 else _min

            print "Case #" + str(i) + ": " + str(_max) + " " + str(_min)
        else:
            ls = put(ls, False)




