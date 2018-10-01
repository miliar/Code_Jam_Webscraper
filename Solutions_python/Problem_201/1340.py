#! /usr/local/bin/python3.5

import sys

import copy

import math


def sol_print(tup):
    value_1, value_2 = tup
    sol_print.line_number += 1
    print("Case #%d: %s %s" % (sol_print.line_number, value_1, value_2))


sol_print.line_number = 0


def nearest_lower_power(x):
    if x < 0:
        return 0

    x -= 1
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return (x + 1) // 2


def nearest_upper_power(x):
    if x < 0:
        return 0

    x -= 1
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return x + 1


# def solve(N, K):
#     # on ajoute 1 parce qu'on veut K + 1 'espace'
#     lower_pow = nearest_lower_power(K + 1)
#     upper_pow = nearest_upper_power(K + 1)
#     print(N, K, lower_pow)
#
#     space = math.ceil(N / lower_pow)
#     # print(space)
#
#     # determine if he's in a small space
#     nb_wide_space = lower_pow - ((space * lower_pow) - N)
#     if K - lower_pow > nb_wide_space:
#         space -= 1
#
#     # reduce due to the previous guys taking places
#     space -= int(math.log(lower_pow, 2))
#
#     # seperate stalls in two
#     res_1 = space // 2
#     res_2 = space - res_1
#     # print(res_1, res_2)
#
#     # because the guy takes one stall
#     if res_1 == res_2:
#         if res_1 != 0:
#             res_1 -= 1
#     else:
#         res_2 -= 1
#
#     return (res_2, res_1)


def get_list_spaces(N, K):
    lower_pow = nearest_lower_power(K + 1)
    lower_log = int(math.log(lower_pow, 2))

    spaces = [N]
    for i in range(lower_log):
        new_spaces = []
        for space in spaces:
            sp_1 = space // 2
            sp_2 = space - sp_1
            if sp_1 == sp_2 and sp_1 != 0:
                sp_1 -= 1
            else:
                sp_2 -= 1
            new_spaces += [sp_1, sp_2]
        spaces = new_spaces
    spaces.sort(reverse=True)
    return spaces


def solve_2(N, K):
    # get sorted list
    spaces = get_list_spaces(N, K)

    lower_pow = nearest_lower_power(K + 1)
    place = K - lower_pow

    chosen_space = spaces[place]

    sp_1 = chosen_space // 2
    sp_2 = chosen_space - sp_1
    if sp_1 == sp_2 and sp_1 != 0:
        sp_1 -= 1
    else:
        sp_2 -= 1

    return (sp_2, sp_1)

T = int(input())
for i in range(T):
    N, K = input().split()
    N, K = int(N), int(K)

    sol_print(solve_2(N, K))
