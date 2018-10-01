#!/usr/bin/env python
# -*- coding: utf-8 -*-

def open_file(file_name):
    with open(file_name) as f:
        line_cnt = int(f.readline())
        case_list = []
        for i in range(0, line_cnt):
            case_list.append([int(i) for i in f.readline().split(" ")])
        return case_list

def solve_one_case(case):
    n = case[0]
    k = case[1]
    dict_parts = dict()
    dict_parts[n] = 1
    max_size = n
    for i in range(0, k - 1):
        if max_size == 1:
            break

        #if max_size in dict_parts:
        max_count = dict_parts[max_size]
        max_count -= 1
        max_size_empty = False
        if max_count == 0:
            del dict_parts[max_size]
            max_size_empty = True
        else:
            dict_parts[max_size] = max_count

        if max_size % 2 == 0:
            small_size = max_size / 2 - 1
            large_size = max_size /2

            if small_size in dict_parts:
                small_count = dict_parts[small_size]
                small_count += 1
                dict_parts[small_size] = small_count
            else:
                dict_parts[small_size] = 1

            if large_size in dict_parts:
                large_count = dict_parts[large_size]
                large_count += 1
                dict_parts[large_size] = large_count
            else:
                dict_parts[large_size] = 1
        else:
            small_size = (max_size - 1) /2
            if small_size in dict_parts:
                small_count = dict_parts[small_size]
                small_count += 2
                dict_parts[small_size] = small_count
            else:
                dict_parts[small_size] = 2

        #if max_size_empty:
        #    if max_size - 1 in dict_parts:
        #        max_size = max_size - 1
        #    else:
        #        if max_size % 2 == 0:
        #            max_size = max_size /2
        #        else:
        #            max_size = (max_size - 1) / 2
        if (len(dict_parts)) == 1:
            return (0,0)

        max_size = max([k[0] for k in dict_parts.items()])

    if max_size % 2 == 0:
        ret_max = max_size /2
        ret_min = max_size / 2 - 1
    else:
        ret_max = ret_min = (max_size - 1) / 2

    return (ret_max, ret_min)


def solve_one_case_fast(case):
    n = case[0]
    k = case[1]
    dict_parts = dict()
    dict_parts[n] = 1
    max_size = n

    while (True):
        # if max_size in dict_parts:
        max_count = dict_parts[max_size]
        k -= max_count
        if k <= 0:
            break

        del dict_parts[max_size]

        if max_size % 2 == 0:
            small_size = max_size / 2 - 1
            large_size = max_size / 2

            if small_size in dict_parts:
                small_count = dict_parts[small_size]
                small_count += max_count
                dict_parts[small_size] = small_count
            else:
                dict_parts[small_size] = max_count

            if large_size in dict_parts:
                large_count = dict_parts[large_size]
                large_count += max_count
                dict_parts[large_size] = large_count
            else:
                dict_parts[large_size] = max_count
        else:
            small_size = (max_size - 1) / 2
            if small_size in dict_parts:
                small_count = dict_parts[small_size]
                small_count += 2 * max_count
                dict_parts[small_size] = small_count
            else:
                dict_parts[small_size] = 2 * max_count

        max_size = max([item[0] for item in dict_parts.items()])

    if max_size % 2 == 0:
        ret_max = max_size / 2
        ret_min = max_size / 2 - 1
    else:
        ret_max = ret_min = (max_size - 1) / 2

    return (ret_max, ret_min)


def solve_all(case_list, out_file):
    with open(out_file, 'w') as f:
        for i, case in enumerate(case_list):
            res = solve_one_case_fast(case)
            """
            Case #1: 1 0
            Case #2: 1 0
            Case #3: 1 1
            Case #4: 0 0
            Case #5: 500 499
            """
            line = "Case #" + str(i + 1) + ": " + str(res[0]) + " " + str(res[1])
            f.write(line)
            f.write("\n")

if __name__ == "__main__":
    #case_list = open_file("test_case")
    #solve_all(case_list, "test_case_out")
    #case_list = open_file("C-small-1-attempt1.in")
    #solve_all(case_list, "C-small-1-attempt1.out")
    #case_list = open_file("C-small-2-attempt1.in")
    #solve_all(case_list, "C-small-2-attempt1.out")
    case_list = open_file("C-large.in")
    solve_all(case_list, "C-large.out")


