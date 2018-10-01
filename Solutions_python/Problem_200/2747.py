#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []


def is_tidy(num_ary):
    tidy = True
    for i in range(len(num_ary) - 1):
        if num_ary[i + 1] - num_ary[i] < 0:
            tidy = False
            break

    return tidy


def to_int(num_ary):
    return int("".join([str(i) for i in num_ary]))


def solve():
    for t in range(ntest):
        N_ary = inputs[t]["N_ary"]
        orig_ary = N_ary[:]
        orig_val = to_int(orig_ary)

        nlen = len(N_ary)
        # print(N_ary)
        for i in range(nlen):
            cur_pos = nlen - i - 1
            prev_pos = nlen - i - 2

            # cur = N_ary[cur_pos]
            prev = N_ary[prev_pos]

            if is_tidy(N_ary):
                # print(i, "maybe tidy")
                N_val = to_int(N_ary)
                if orig_val < N_val:
                    N_ary[prev_pos] = N_ary[prev_pos] - 1
                # print(N_ary)
                # break

            if not is_tidy(N_ary):
                N_ary[cur_pos] = 9
                N_ary[prev_pos] = 9 if prev == 0 else prev - 1
            # print(i, N_ary)

        result = to_int(N_ary)

        print("Case #{0}: {1}".format(t + 1, result))


def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for n in range(ntest):
        N_ary = [int(c) for c in sys.stdin.readline().strip()]
        inputs.append({"N_ary": N_ary})
    # pp.pprint(inputs)


if __name__ == '__main__':
    parse()
    solve()
