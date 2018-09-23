#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


import sys


def do(N, K):
    if N == K:
        return (0, 0)
    stalls = [1] + [0] * N + [1]
    unoc = set(range(1, N + 1))

    def ls(stalli):
        return next(stalli - index - 1 for index
                    in range(stalli, -1, -1) if stalls[index] == 1)

    def rs(stalli):
        return next(index - stalli - 1 for index in
                    range(stalli, N + 2, 1) if stalls[index] == 1)

    for _ in range(K):
        stalli, l, r = next(iter(sorted(((index, ls(index), rs(index))

                                      for index in unoc),
                                      key=lambda t: (min(t[1], t[2]), max(t[1], t[2]), -t[0]),
                                      reverse=True)))
        stalls[stalli] = 1
        unoc -= {stalli}
    return max(l, r), min(l, r)


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        with open(filename.replace(".in", ".out"), "w") as f2:
            for i, line in enumerate(f.readlines()):
                if i != 0:
                    a = int(line.strip().split(" ")[0])
                    b = int(line.strip().split(" ")[1])
                    c, d = do(a, b)
                    f2.write("Case #{}: {} {}\n".format(i, c, d))
