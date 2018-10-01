def prt(case, n):
    print "Case #%s: %s" % (case + 1, n)

for case in xrange(int(raw_input())):
    change_index = -1
    s = raw_input()

    l = len(s)
    if l == 1:
        prt(case, int(s))
        continue

    for i, d in enumerate(s[:-1]):
        if d > s[i + 1]:
            change_index = i

            s2 = s[:i]
            for i2, d2 in enumerate(s2[::-1]):
                if d2 == d:
                    change_index = i - i2 - 1
            break

    if change_index < 0:
        prt(case, int(s))
        continue

    change_index = change_index

    prt(case, int(s[:change_index] + str(int(s[change_index]) - 1) + '9' * (l - change_index - 1)))
    #print "Case %s: %s" % (case + 1, int(s[:change_index] + str(int(s[change_index]) - 1) + '9' * (l - change_index - 1)))
