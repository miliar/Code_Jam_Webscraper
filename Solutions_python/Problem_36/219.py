#!/usr/bin/pyhon

import sys


""" usage: python task_c.py input_file_name

Requires python 2.x
"""


f = open(sys.argv[1])
count = int(f.readline())
for case_no in range(1, count + 1):
    line = f.readline().strip()
    len_line = len(line)
    s = "welcome to code jam"
    a = [0 for c in line]
    for si in range(len(s)):
        cs = s[len(s) - si - 1]
        for i in reversed(range(len_line)):
            if i >= len_line - si:
                a[i] = 0
            elif i == len_line - si - 1:
                if line[i] == cs:
                    if si == 0:
                        a[i] = 1
                    else:
                        if a[i] > 0:
                            a[i] = 1
                        else:
                            a[i] = 0
                else:
                    a[i] = 0
            else:
                if line[i] == cs:
                    if si == 0:
                        a[i] = (a[i + 1] + 1) % 10000
                    else:
                        if a[i] != 0:
                            a[i] = (a[i] + a[i + 1]) % 10000
                else:
                    a[i] = a[i + 1]
    print "Case #%d: %.4d" % (case_no, a[0])
