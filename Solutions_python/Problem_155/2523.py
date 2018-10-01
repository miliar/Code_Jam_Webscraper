__author__ = 'fdoherty'

from sys import stdin


def output(case, data):
    print 'Case #%s:' % case, data


def solve(case_num, max, code):
    required = 0
    audience = 0
    for x in range(max+1):
        required_x = 0
        if x > audience:
            required_x = x - audience
        required += required_x
        audience_x = int(code[x])
        audience += audience_x + required_x
    output(case_num, required)


NUM_CASES = int(stdin.readline())

for n in range(NUM_CASES):
    args = {}
    line = stdin.readline().strip()

    (MAX, CODE) = line.split(' ')
    solve(n+1, int(MAX), CODE)