def show(i, val):
    print "Case #%s: %s" % (i, val)


def to_list(n):
    ret = []

    while n != 0:
        ret.append(n % 10)
        n /= 10

    return ret[::-1]


def to_num(lst):
    multi, ret = 1, 0
    for el in lst[::-1]:
        ret += multi * el
        multi *= 10

    return ret


def sol(n):
    if n < 10:
        return n
    lst = to_list(n)
    ll = len(lst)

    tidy = True
    for i in xrange(ll - 1):
        if lst[i] > lst[i + 1]:
            tidy = False
            break

    if tidy:
        return n

    c = ll - 2
    while c != -1:
        if lst[c] > lst[c + 1]:
            lst[c] -= 1
            for i in xrange(c + 1, ll):
                lst[i] = 9
        c -= 1

    if lst[0] == 0:
        return to_num(lst[1:]) # all 9
    else:
        return to_num(lst)


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        n = int(raw_input().strip())
        show(i, sol(n))

