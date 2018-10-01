def is_tidy_num(l):
    tidy_num = False
    pos_failed = 0

    for i in xrange(0, len(l) - 1):
        if l[i + 1] and int(l[i]) <= int(l[i+1]):
            tidy_num = True
        else:
            tidy_num = False
            pos_failed = i
            break

    return {
        'tidy_num': tidy_num,
        'pos_failed': pos_failed
    }


def tidy_num(l, pos_failed):
    if pos_failed == 0:
        if l[0] == 1:
            l.remove(l[0])
            l = [9 for x in l]
        else:
            l[0] -= 1
            l = [l[0]] + [9 for x in l[:-1]]

    if pos_failed != 0:
        l[pos_failed] -= 1
        l = l[:pos_failed+1] + [9 for x in l[pos_failed+1:]]

    return l


t = int(raw_input())

for i in xrange(1, t + 1):
    l = [int(x) for x in raw_input()]

    while True:
        if len(l) == 1:
            print "Case #{}: {}".format(i, l[0])
            break
        tidy_num_obj = is_tidy_num(l)
        if tidy_num_obj['tidy_num']:
            print "Case #{}: {}".format(i, "".join(str(i) for i in l))
            break
        else:
            l = tidy_num(l, tidy_num_obj['pos_failed'])
