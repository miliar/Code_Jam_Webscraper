#!/bin/python

import sys, math

def init_stalls(n):
    s = [0] * (n + 2)
    s[0] = 1
    s[-1] = 1

    return s

def occupy(stalls, scores, pos):
    keys = scores.keys()
    pos_cur = keys.index(pos)

    # left
    cur = pos_cur - 1
    while cur >= 0:
        prev_key = keys[cur + 1]
        now_key = keys[cur]

        prev = scores[prev_key]
        now = scores[now_key]

        if cur == pos_cur - 1:
            new_left_count = 0
        elif prev_key - now_key > 1:
            break
        else:
            new_left_count = prev[1] + 1

        scores[keys[cur]] = (now[0], max(new_left_count, 0))
        cur -= 1

    # print "after left: {}".format(scores)
    # right
    cur = pos_cur + 1
    carry = 0
    while cur < len(scores):
        prev_key = keys[cur - 1]
        now_key = keys[cur]

        prev = scores[prev_key]
        now = scores[now_key]

        if cur == pos_cur + 1:
            new_right_count = 0
        elif now_key - prev_key> 1:
            break
        else:
            new_right_count = prev[0] + 1

        scores[keys[cur]] = (max(new_right_count, 0), now[1])
        cur += 1


    # print "after right: {}".format(scores)
    stalls[pos] = 1
    return scores.pop(pos)

def num_empty_left(stalls, pos):
    cur = pos - 1
    n = 0

    while cur > 0 and stalls[cur] == 0:
        n += 1
        cur -= 1

    return n

def num_empty_right(stalls, pos):
    cur = pos + 1
    n = 0

    while cur < len(stalls) and stalls[cur] == 0:
        n += 1
        cur += 1

    return n

def calculate_score(stalls, pos):
    return (num_empty_left(stalls, pos), num_empty_right(stalls, pos))

def calculate_scores(stalls):
    scores = {}
    for i in xrange(len(stalls)):
        if stalls[i] == 0:
            scores[i] = calculate_score(stalls, i)

    return scores

def sort_by_cond(scores, cand, func):
    tmp = sorted(cand, key=lambda x: -func(scores[x]))

    new_cand = []
    m = func(scores[tmp[0]])
    cur = 0
    while(cur < len(tmp) and func(scores[tmp[cur]]) == m):
        new_cand.append(tmp[cur])
        cur += 1

    return new_cand

def get_optimal_pos(stalls, scores):
    cand = scores.keys()
    cand1 = sort_by_cond(scores, cand, min)
    cand2 = sort_by_cond(scores, cand1, max)
    return sorted(cand2)[0]

def solve(stalls, num_people):
    scores = {}
    pos = None

    scores = calculate_scores(stalls)

    ans = None
    for p in xrange(num_people):
        pos = get_optimal_pos(stalls, scores)
        ans = occupy(stalls, scores, pos)

    return max(ans), min(ans)

num_cases = input()
for i in xrange(num_cases):
    n, p = raw_input().split(' ')

    stalls = init_stalls(int(n))
    num_people = int(p)

    ans = solve(stalls, num_people)
    print "Case #{}: {} {}".format(i + 1, ans[0], ans[1])
