import sys
import re


inf = sys.stdin
outf = sys.stdout

def op(c):
    if c == '+':
        return '-'
    return '+'

def handle_case(case_num):
    cakes_str, k_str = inf.readline().strip().split()
    cakes = [1 if c == '+' else 0 for c in cakes_str]
    # print cakes
    k = int(k_str)
    n = 0
    for i, v in enumerate(cakes):
        if i + k > len(cakes):
            break
        if v == 1:
            continue
        for shift in xrange(k):
            cakes[i + shift] = 1 - cakes[i + shift]
        n += 1
        # print cakes

    if 0 in cakes:
        res = 'IMPOSSIBLE'
    else:
        res = str(n)
    case_str = 'Case #{0}: {1}'.format(case_num, res)
    print >>outf, case_str


def main():
    if len(sys.argv) > 1:
        global inf
        inf = open(sys.argv[1])
    if len(sys.argv) > 2:
        global outf
        outf = open(sys.argv[2], 'w')

    T = int(inf.readline().strip())
    for case_num in xrange(1, T+1):
        handle_case(case_num)

    if inf != sys.stdin:
        inf.close()
    if outf != sys.stdout:
        outf.close()


if __name__ == '__main__':
    main()
