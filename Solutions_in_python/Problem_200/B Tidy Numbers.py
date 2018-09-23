#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Name:        Google Code Jam 2017 - Qualifiers - Tidy Numbers
#
# Author:      Ashish Nitin Patil
#
# Created:     08-04-2017
# Copyright:   (c) Ashish Nitin Patil 2017
# Licence:     New BSD License
#-------------------------------------------------------------------------------

T = int(input())

def tidy(N):
    N = str(N)
    len_N = len(N)
    for i in range(len_N-1, 0, -1):
        # print(i, N)
        if N[i] < N[i-1]:
            prev = N[:i-1] if i != 1 else ''
            N = prev + str(int(N[i-1]) - 1) + '9'*(len_N-i)
    return int(N)

for test_case in range(1, T+1):
    N = int(input())
    answer = tidy(N)
    print("Case #{0}: {1}".format(test_case, answer))
