import os
import sys

debug_mode = False
if debug_mode:
    debug_fd = sys.stdout
else:
    debug_fd = open(os.devnull, "w")


def read_input():
    line = raw_input()
    pancakes_str, k_str = line.split()
    k = int(k_str)
    pancakes = list(pancakes_str)
    return pancakes, k

def calculate(input_args):
    pancakes, k = input_args

    def neg(side):
        if side == "+":
            return "-"
        elif side == "-":
            return "+"
        else:
            raise Exception("In neg: " + side)

    idx = 0
    l = len(pancakes)
    flip_cnt = 0
    while idx + k <= l:
        if pancakes[idx] == "-":
            flip_cnt += 1
            for _ in xrange(k):
                pancakes[idx+_] = neg(pancakes[idx+_])
        idx += 1
    while idx < l:
        if pancakes[idx] == "-":
            return "IMPOSSIBLE"
        idx += 1
    return flip_cnt

def to_formated_string(result_tokens):
    return result_tokens

if __name__ == '__main__':
    T = int(raw_input())
    case = 1
    while case <= T:
        input_args = read_input()
        result = calculate(input_args)
        answer = to_formated_string(result)
        print 'Case #%d:' % case, answer
        case += 1

