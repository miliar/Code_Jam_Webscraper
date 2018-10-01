# -*- coding: utf-8 -*-
# @Author: Pandarison
# @Date:   2017-04-08
# @Last Modified time: 2017-04-08

T = int(input())
for case_id in range(1, T+1):
    N = list(map(int, list(input())))
    for i in range(len(N)-1, 0, -1):
        if N[i] < N[i-1]:
            for j in range(i, len(N)):
                N[j] = 9
            N[i-1] -= 1
    print("Case #%d: "%case_id + str(int("".join(list(map(str, N))))))