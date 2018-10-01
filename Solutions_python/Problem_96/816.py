#!/usr/bin/python

import sys
from collections import defaultdict

def build_scores():
    tuples = [(score, i, j, k, i - k == 2)
        for score in range(0, 31) for i in grades for j in grades for k in grades
        if i >= j and j >= k and i - k <= 2 and i + j + k == score]
    result = defaultdict(list)
    for score, i, j, k, surprising in tuples:
        result[score].append((i, j, k, surprising))
    return result;

def generate(S, pointss, index, num_surprising, solution, solutions):
    if index == len(pointss):
        if num_surprising == S:
            solutions.append(list(solution))
        return
    for score in scores[pointss[index]]:
        solution[index] = score
        new_num_surprising = num_surprising
        if (score[3]):
            new_num_surprising += 1
        generate(S, pointss, index + 1, new_num_surprising, solution, solutions)

def solve(case):
    N = int(case[0])
    S = int(case[1])
    p = int(case[2])
    pointss = map(int, case[3:])
    
    solutions = []
    
    generate(S, pointss, 0, 0, [() for points in pointss], solutions)

    solutions = filter(lambda s: len(filter(lambda x: x[3], s)) == S, solutions)
    ps = sorted(map(lambda s: len(filter(lambda score: score[0] >= p, s)), solutions), reverse = True)
    if len(ps) == 0:
        return 0
    return ps[0]

grades = range(0, 11)
scores = build_scores()
solution_counter = 0

input = [line.strip().split() for line in sys.stdin]

for index in range(1, int(input[0][0]) + 1):
    print 'Case #%d: %d' % (index, solve(input[index]))
