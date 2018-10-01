import math


def syrup(n, k, ps):
    sorted_ps = sorted(ps, key=lambda (r, h): (r, h), reverse=True)
    rem_ps = iter_rem(sorted_ps, k)
    return calc_area_list(rem_ps)


def iter_rem(ps, k):
    if k == len(ps):
        return ps
    min_diff = float("inf")
    min_diff_index = -1
    for i in range(len(ps)):
        diff = calc_diff(i, ps)
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i
    ps.pop(min_diff_index)
    return iter_rem(ps, k)


def calc_diff(i, ps):
    (r, h) = ps[i]
    if len(ps) == 1:
        return calc_area(r, h)
    if i == len(ps) - 1:
        return calc_area_side(r, h)
    (r2, _) = ps[i + 1]
    if i == 0:
        return calc_area_min_next(r, h, r2)
    return calc_area_side(r, h)


def calc_area_list(ps):
    res = 0
    for i in range(len(ps)):
        (r, h) = ps[i]
        if i == len(ps) - 1:
            res += calc_area(r, h)
        else:
            (r2, _) = ps[i + 1]
            res += calc_area_min_next(r, h, r2)
    return res


def calc_area(r, h):
    return calc_area_top(r) + calc_area_side(r, h)


def calc_area_min_next(r1, h1, r2):
    return calc_area(r1, h1) - calc_area_top(r2)


def calc_area_top(r):
    return math.pi * r * r


def calc_area_side(r, h):
    return 2 * math.pi * r * h


input_t = int(raw_input())
for i in xrange(1, input_t + 1):
    i_n, i_k = [int(st) for st in raw_input().split(" ")]
    i_ps = []
    for i2 in xrange(i_n):
        i_r, i_h = [int(st2) for st2 in raw_input().split(" ")]
        i_ps.append((i_r, i_h))
    result = syrup(i_n, i_k, i_ps)
    print "Case #{}: {}".format(i, result)
