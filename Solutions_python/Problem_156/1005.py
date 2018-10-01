#!/usr/bin/env python
import heapq
from itertools import combinations
import math
import sys


def problem(j, fi):
    n = int(fi.readline().strip())
    plates = map(int, fi.readline().strip().split(' '))
    return n, plates

def solve(params, problem_id):
    n, plates = params

    m = {}
    for plate in plates:
        if not plate in m:
            m[plate] = [-plate, 0]
        m[plate][1] += 1

    h = m.values()
    heapq.heapify(h)

    def solution(h):
        max_val, count = -h[0][0], h[0][1]
        if max_val == 1:
            return 1
#        if max_val < count + math.ceil(max_val / 2):
#            return max_val

        heapq.heappop(h)
        # del m[max_val]


        # if max_val % 2:
        #     insert_vals = [(max_val / 2, count),
        #                    (max_val / 2 + 1, count)]
        # else:
        #     insert_vals = [(max_val / 2, 2 * count)]

# def test(max_val, count):
        split_max_val = None
        splits_cands = []

        for splits in xrange(1, (max_val + 2) / 2):
            base = max_val / (splits + 1)
            left = max_val % (splits + 1)
            vals = []
            new_split_max_val = base + 1 if left else base

            if split_max_val and new_split_max_val >= split_max_val:
                continue
            # print ((splits, base, left), weight)
            splits_cands.append(((splits, base, left), [h_el[:] for h_el in h]))

        weights = [max_val]
        for best_split, new_h in splits_cands:

            insert_vals = []
            splits, base, left = best_split
            for i in xrange(splits + 1):
                val = base + 1 if left else base
                if left:
                    left -= 1
                insert_vals.append((val, count))

            # print max_val, insert_vals

            for val, c in insert_vals:
                for el in new_h:
                    if el[0] == -val:
                        el[1] += c
                        break
                else:
                    heapq.heappush(new_h, [-val, c])

            weights.append((count * splits) + solution(new_h))

        return min(weights)

    return solution(h)


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(1, total + 1):
            print "Processing case #{0}".format(i)
            res = solve(problem(i, fi), i)
            fo.write('Case #{0}: {1}\n'.format(i, res))
            fo.flush()
