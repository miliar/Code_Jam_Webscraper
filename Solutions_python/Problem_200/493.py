import os
import sys

debug_mode = False
if debug_mode:
    debug_fd = sys.stdout
else:
    debug_fd = open(os.devnull, "w")


def read_input():
    N = int(raw_input())
    return N

def calculate(input_args):
    N = input_args

    mask = 10
    while True:
        l = N / mask  # left
        if l == 0:
            break
        r = N % mask  # right
        l_digit = l % 10  # lowest digit of left part
        r_digit = r / (mask / 10)  # rightmost digit of right part
        #print "[%s][%s], %d, %d" % (l, r, l_digit, r_digit)
        if l_digit > r_digit:
            N -= (r + 1)
            #print N
        mask *= 10

    return N

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

