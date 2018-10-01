import sys
import itertools

for case in xrange(int(raw_input())):
    q, p = map(int, raw_input().split())

    cells = [i for i in xrange(1, q + 1)]
    to_release = map(int, raw_input().split())

    min_coins = sys.maxint
    for permutation in itertools.permutations(to_release):
        c = cells[:]
        coins = len(c) - 1
        c[permutation[0] - 1] = None
        for indx, item in enumerate(permutation[1:]):
            c[item - 1] = None
            start = 0
            while True:
                try:
                    new_start = c.index(None, start)
                    if new_start >= item - 1:
                        break
                    start = new_start + 1
                except ValueError:
                    break
            try:
                end = c.index(None, item)
            except ValueError:
                end = len(c)
            coins += abs(item - start - 1) + abs(end - item)
            if coins > min_coins:
                break
        if coins < min_coins:
            min_coins = coins

    print 'Case #%d: %d' % (case + 1, min_coins)
