# /usr/bin/env python
# -*- coding: utf8 -*-


def Ls(half_bath):
    sz = len(half_bath) - 1
    for i in range(sz + 1):
        if half_bath[sz - i] == "o":
            return i
    return sz + 1


def Rs(half_bath):
    sz = len(half_bath) - 1
    for i in range(sz + 1):
        if half_bath[i] == "o":
            return i
    return sz + 1


def test(bathroom):
    min_lr = [0 for e in bathroom]
    max_lr = [0 for e in bathroom]
    for i, stall in enumerate(bathroom):
        if stall != "o":
            ls = Ls(bathroom[:i])
            rs = Rs(bathroom[i + 1:])
            min_lr[i] = min(ls, rs)
            max_lr[i] = max(ls, rs)
        else:
            min_lr[i] = -1e13
            max_lr[i] = -1e13
    maxima = max(min_lr)
    if min_lr.count(maxima) > 1:
        sub = [mx for mx, mn in zip(max_lr, min_lr) if mn == maxima]
        # print("sub :", sub)
        index = max_lr.index(max(sub))
    else:
        index = min_lr.index(maxima)
    bathroom[index] = "o"
    # print(bathroom)
    return (max_lr[index], min_lr[index])


def test3(bathroom):
    min_lr = [0 for e in bathroom]
    max_lr = [0 for e in bathroom]
    for i, stall in enumerate(bathroom):
        if stall != "o":
            ls = Ls(bathroom[:i])
            rs = Rs(bathroom[i + 1:])
            print(i,(ls, rs), "\t", bathroom[:i], [stall], bathroom[i + 1:])
            min_lr[i] = min(ls, rs)
            max_lr[i] = max(ls, rs)
            print("\t", min_lr[i], max_lr[i])
        else:
            min_lr[i] = -1e13
            max_lr[i] = -1e13
    maxima = max(min_lr)
    print("we choose :", maxima, ". with ", min_lr.count(maxima), "occurences")
    if min_lr.count(maxima) > 1:
        sub = [mx for mx, mn in zip(max_lr, min_lr) if mn == maxima]
        print("sub :", sub, "->", max(sub), max_lr.index(max(sub)))
        index = max_lr.index(max(sub))
    else:
        index = min_lr.index(maxima)
    bathroom[index] = "o"
    # print(bathroom)
    return max_lr[index], min_lr[index], bathroom


def test4(bathroom):
    min_lr = [0 for e in bathroom]
    max_lr = [0 for e in bathroom]
    min_max = [0 for e in bathroom]
    for i, stall in enumerate(bathroom):
        if stall != "o":
            ls = Ls(bathroom[:i])
            rs = Rs(bathroom[i + 1:])
            # print(i,(ls, rs), "\t", bathroom[:i], [stall], bathroom[i + 1:])
            min_lr[i] = min(ls, rs)
            max_lr[i] = max(ls, rs)
            min_max[i] = (min_lr[i], max(ls, rs))
            # print("\t", min_lr[i], max_lr[i])
        else:
            min_lr[i] = -1e13
            max_lr[i] = -1e13
    maxima = max(min_lr)
    # print("we choose :", maxima, ". with ", min_lr.count(maxima), "occurences")
    if min_lr.count(maxima) > 1:
        # sub = [mx for mx, mn in zip(max_lr, min_lr) if mn == maxima]
        sub = [mxn for mxn, mn in zip(min_max, min_lr) if mn == maxima]
        # print("sub :", sub, "->", max(sub), max_lr.index(max(sub)))
        index = min_max.index(max(sub))
    else:
        index = min_lr.index(maxima)
    bathroom[index] = "o"
    # print(bathroom)
    return max_lr[index], min_lr[index], bathroom



if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        N, K = [int(e) for e in input().split()]
        bathroom = ["-"] * N
        bathroom = ["o"] + bathroom + ["o"]
        # print(bathroom)
        for people in range(K):
            mx, mn, bathroom = test4(bathroom)
            # print(bathroom)
        print("Case #{}: {} {}".format(ti + 1, mx, mn))
        # if ti == 3:
        #     break
