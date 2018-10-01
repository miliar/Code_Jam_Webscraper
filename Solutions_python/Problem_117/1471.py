#!/usr/bin/env python2
# b

with open("b.in") as f:
    k = int(f.readline().strip())

    for kk in xrange(k):
        x, y = map(int, f.readline().strip().split())

        field = []
        for xx in xrange(x):
            field.append(f.readline().strip().replace(' ', ''))

        max_ys = [None] * y

        lock_x = [False] * x
        lock_y = [False] * y

        try:
            for xx in xrange(x):
                max_x = max(field[xx])
                for yy in xrange(y):
                    if max_ys[yy] is None:
                        max_ys[yy] = max((field[j][yy] for j in xrange(x)))

                    max_y = max_ys[yy]

                    this = field[xx][yy]

                    if (lock_y[yy] and this >= max_y) or \
                       (lock_x[xx] and this >= max_x):
                        continue

                    if (lock_y[yy] and this < max_y) or \
                       (lock_x[xx] and this < max_x):
                        raise Exception("%s %s" % (xx, yy))

                    if not lock_x[xx] and this < max_y:
                        lock_x[xx] = True

                    if not lock_y[yy] and this < max_x:
                        lock_y[yy] = True

                    if lock_x[xx] and lock_y[yy]:
                        raise Exception("%s %s" % (xx, yy))


        except Exception as exc:
            print "Case #{0}: NO".format(kk + 1)
        else:
            print "Case #{0}: YES".format(kk + 1)
