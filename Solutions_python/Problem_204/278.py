#!/usr/bin/env python3

import functools
import math
import sys


@functools.lru_cache(maxsize=100500)
def maxpack(packages):
    #print("So its maxpaxk for", packages)
    res = 0
    for p in packages:
        setp = set(p)
        for x in p:
            new_packages = tuple(pack for pack in packages if not set(pack) & setp)
            res = max(res, 1 + maxpack(new_packages))
    return res


def decmul(vlist, idx):
    for v in vlist[0]:
        if not vlist[1:]:
            yield [(idx, v)]
        else:
            for dm in decmul(vlist[1:], idx+1):
                yield [(idx, v)] + dm


def solve(n, p, rs, quants):
    maxpack.cache_clear()
    rs_limits = [(r*0.9, r*1.1) for r in rs]

    quants = list(sorted(q, key=lambda x: -x) for q in quants)
    quants_as_limits = [
        [list(range(int(math.ceil(q/r[1])), int(q/r[0])+1))
            for q in quant]
        for quant, r in zip(quants, rs_limits)]

    count_to_variants = {}

    for qi, ql in enumerate(quants_as_limits):
        for i, valtup in enumerate(ql):
            for val in valtup:
                if val not in count_to_variants:
                    if qi != 0:
                        continue
                    else:
                        count_to_variants[val] = [None] * len(quants)
                if count_to_variants[val][qi] is None:
                    count_to_variants[val][qi] = [i]
                else:
                    count_to_variants[val][qi].append(i)

    count_to_variants = {c: v for c, v in count_to_variants.items()
                         if all(x is not None for x in v)}

    # print(quants_as_limits)
    # print(count_to_variants)

    packages = set()
    for vlist in count_to_variants.values():
        # print(vlist)
        dm = list(map(tuple, decmul(vlist, 0)))
        # print(dm)
        packages |= set(map(tuple, decmul(vlist, 0)))
    # print(packages)
    return maxpack(tuple(packages))


def solve_inputs(inputs):
    cnt = int(inputs[0])
    inputs = inputs[1:]
    for i in range(cnt):
        n, p = map(int, inputs[0].split())
        rs = list(map(int, inputs[1].split()))
        quants = [list(map(int, inputs[2+j].split())) for j in range(n)]
        print("Case #{}:{}".format(i + 1, solve(n, p, rs, quants)))
        inputs = inputs[2+n:]


def main():
    solve_inputs(sys.stdin.readlines())

if __name__ == '__main__':
    main()
