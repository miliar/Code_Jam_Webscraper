#! /usr/bin/env python3
#  codejam 2015 xykhl 1A 1
import sys
stdin = sys.stdin

def solve(smax, shydata):
    n_clamping = 0
    n_toinvite_total = 0

    for (shylvl, x) in enumerate(shydata):
        if x == 0:
            continue
        n_toinvite = max(shylvl - n_clamping, 0)
        n_clamping += x + n_toinvite
        n_toinvite_total += n_toinvite

    return n_toinvite_total


def process_data_line(s):
    smax_s, data_s = s.split(' ', 1)
    smax = int(smax_s)
    l = list(map(int, list(data_s)))
    assert len(l) == smax + 1
    assert l[-1] != 0
    return (smax, l)


def main():
    n = int(stdin.readline().strip())
    assert n > 0

    for i in range(n):
        data = process_data_line(stdin.readline().rstrip("\n"))
        result = solve(*data)
        print("Case #{}: {}".format(i+1, result))


if __name__ == "__main__":
    main()
