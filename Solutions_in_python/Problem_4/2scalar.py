#!/usr/bin/python

import sys, string

num = int(sys.stdin.readline())

def reduce (vec_A, vec_B, num):
        if (vec_A == []):
                return 0

        min_A = min(vec_A)
        pos_min_A = vec_A.index(min_A)
        min_B = min(vec_B)
        pos_min_B = vec_B.index(min_B)
        max_A = max(vec_A)
        pos_max_A = vec_A.index(max_A)
        max_B = max(vec_B)
        pos_max_B = vec_B.index(max_B)

        if (abs(max_A - min_B) > abs(max_B - min_A)):
                if (pos_max_A != pos_min_B):
                        num = num - 1
                vec_A[pos_max_A], vec_A[pos_min_B] = vec_A[pos_min_B], vec_A[pos_max_A]
                del vec_A[pos_min_B], vec_B[pos_min_B]
                return (max_A * min_B) + reduce(vec_A, vec_B, num)
        else:
                if (pos_min_A != pos_min_B):
                        num = num - 1
                vec_A[pos_min_A], vec_A[pos_max_B] = vec_A[pos_max_B], vec_A[pos_min_A]
                del vec_A[pos_max_B], vec_B[pos_max_B]
                return (min_A * max_B) + reduce(vec_A, vec_B, num)

for case in range(num):
        vec_len = int(sys.stdin.readline())
        vec_A = sys.stdin.readline().split()
        vec_B = sys.stdin.readline().split()

        vec_A_int = [int(x) for x in vec_A]
        vec_B_int = [int(x) for x in vec_B]

        sum = reduce(vec_A_int, vec_B_int, 2)

        print "Case #" + str(case+1) + ": ", sum
