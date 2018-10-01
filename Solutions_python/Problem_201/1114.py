#!/usr/bin/env python3
import math

def get_h(n):
    return math.floor(math.log(n, 2))

def get_floor_head(n, h):
    if h == 0:
        return n
    return math.floor(n / math.pow(2, h))

def get_full_range(n, h):
    if h == 0:
        return 1
    head = get_floor_head(n, h)
    k = (head + 1) * math.pow(2, h) - n - 1
    return math.pow(2, h) - k

def get_nth(no_people, no_stall):
    height = get_h(no_people)
    head = get_floor_head(no_stall, height)
    offset = no_people - int(math.pow(2, height))
    full_range = get_full_range(no_stall, height)
    if offset < full_range:
        return head
    else:
        return head - 1

def get_ls_rs(size):
    if size <= 1:
        return (0, 0)

    half = int(size/2)
    if size%2 == 0:
        return (half - 1, half)
    return (half, half)

def solve(case_number, no_stall, no_people):
    size = get_nth(no_people, no_stall)
    t = get_ls_rs(size)
    print_ans(case_number, "%d %d"%(max(t), min(t)))

def print_ans(case_number, answer):
    print("Case #%d: %s"%(case_number, answer))

no_test = int(input())
line_num = 1
while no_test > 0:
    sp = input().split(' ')
    solve(line_num, int(sp[0]), int(sp[1]))
    no_test -= 1
    line_num += 1
