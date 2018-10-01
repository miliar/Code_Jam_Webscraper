#!/usr/bin/env python
import sys


def problem(fi):
    n, r, o, y, g, b, v = fi.readline().strip().split(' ')
    return map(int, (n, r, o, y, g, b, v))


def solve(params, i):
    n, r, o, y, g, b, v = params

    pets = {
        'R': r,
        'O': o,
        'Y': y,
        'G': g,
        'B': b,
        'V': v,
    }

    res = [None] * n
    last_color = None
    # selection = False

    prio = {
        color: i
        for i, (count, color) in enumerate(sorted((count, color) for color, count in pets.iteritems()))
    }

    assert pets['O'] == 0 and pets['G'] == 0 and pets['V'] == 0
    assert pets['R'] + pets['Y'] + pets['B'] == n

    # print prio, pets

    for i in xrange(n):
        count, _, color = max((c, prio[colors], colors) for colors, c in pets.iteritems() if colors != last_color)

        if count == 0:
            return 'IMPOSSIBLE'

        # if i == 0:
        #     first_color = color

        # if not selection and all(c in (0, 1) for c in pets.itervalues()):
        #     if color != first_color and pets[first_color] and last_color != first_color:
        #     # if pets[first_color] and last_color != first_color:
        #         selection = True
        #         color = first_color

        res[i] = color
        last_color = color
        pets[color] -= 1

    assert pets['O'] == 0 and pets['G'] == 0 and pets['V'] == 0

    # print ''.join(res)
    if res[0] == res[-1]:
        return 'IMPOSSIBLE'

    for i in xrange(n - 1):
        if res[i] == res[i + 1]:
            print ''.join(res)
            raise ValueError('Should not happen')

    return ''.join(res)


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
