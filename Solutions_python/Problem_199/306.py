#!/usr/bin/env python
# -*- coding: utf-8 -*-

def open_file(file_name):
    with open(file_name) as f:
        line_cnt = int(f.readline())
        case_list = []
        for i in range(0, line_cnt):
            case_line = f.readline()
            line_items = case_line.split(" ")
            k = int(line_items[1])
            case = [True if c=='+' else False for c in line_items[0]]
            case_list.append([k, case])
        return case_list

def solve_one_case(case):
    k = case[0]
    p = case[1]
    len_p = len(p)
    count = 0
    impossible = False
    for i in range(0, len_p):
        c = p[i]
        if c == False:
            if i + k > len_p:
                impossible = True
                break
            else:
                for j in range(i, i + k):
                    p[j] = not p[j]
                count += 1
    return (impossible, count)

def solve_all(case_list, out_file):
    with open(out_file, 'w') as f:
        for i, case in enumerate(case_list):
            res = solve_one_case(case)
            """
            Case #1: 3
            Case #2: 0
            Case #3: IMPOSSIBLE
            """
            line = "Case #" + str(i + 1) + ": " + (str(res[1]) if res[0] is False else "IMPOSSIBLE")
            f.write(line)
            f.write("\n")

if __name__ == "__main__":
    #case_list = open_file("test_case")
    #solve_all(case_list, "test_case_out")
    #case_list = open_file("A-small-attempt0.in")
    #solve_all(case_list, "A-small-attempt0.out")
    case_list = open_file("A-large.in")
    solve_all(case_list, "A-large.out")


