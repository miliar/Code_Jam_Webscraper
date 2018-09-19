#!/usr/bin/python
#
# author: tzeng.yuxio@gmail.com
# usage: cat file.input | ./qround-problem-d.py > file.output

import sys

def solve():
    numblocks = (int)(sys.stdin.readline())
    s = sys.stdin.readline()[:-1]
    wn = [float(x) for x in s.split()]
    s = sys.stdin.readline()[:-1]
    wk = [float(x) for x in s.split()]

    wn.sort()
    wk.sort()

    str_dwar = ""
    while wn or wk:
        if not wn:
            str_dwar += "X"
            wk.pop()
        elif not wk:
            str_dwar += "O"
            wn.pop()
        elif wn[-1] > wk[-1]:
            str_dwar += "O"
            wn.pop()
        else:
            str_dwar += "X"
            wk.pop()

    naomi_count = 0
    ken_count = 0
    naomi_win = 0
    ken_win = 0
    for c in str_dwar:
        if c == 'O':
            naomi_count += 1
            if ken_count > 0:
                ken_count -= 1
                ken_win += 1
        else:
            ken_count += 1
            if naomi_count > 0:
                naomi_count -= 1
                naomi_win += 1

    return repr(naomi_win) + " " + repr(numblocks - ken_win)
    # return str_dwar

t = (int)(sys.stdin.readline())
for i in range(t):
    print 'Case #' + repr(i+1) + ': ' + solve()
