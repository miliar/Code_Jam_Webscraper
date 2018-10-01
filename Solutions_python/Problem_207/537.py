from __future__ import division


def parse_input(str_test):
    t = str_test.split()
    return map(int, t)


def ind_max(values, ind):
    val_copy = values[:]
    if ind != -1:
        val_copy[ind] = 0
    return max(xrange(len(val_copy)), key=val_copy.__getitem__)
    # values.index(max(values))


def solve(test):
    N, R, O, Y, G, B, V = test

    colors = [R, Y, B]

    color_sort = [i[0] for i in sorted(enumerate(colors), key=lambda x: x[1])][::-1]
    colors.sort(reverse=True)

    if max(colors) * 2 > sum(colors):
        return "IMPOSSIBLE"

    res_c = []
    prev_c = -1
    for i in range(N):
        c_ind = ind_max(colors, prev_c)
        prev_c = c_ind
        colors[c_ind] = colors[c_ind] - 1
        res_c.append(c_ind)

    colors_char = ['R','Y','B']
    res = []
    for c_ind in res_c:
        res.append(colors_char[color_sort[c_ind]])

    assert all(c == 0 for c in colors)
    assert len(res) == N
    return ''.join(res)
