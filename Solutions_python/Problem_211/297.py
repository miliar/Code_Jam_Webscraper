#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

T = int(input())  # number of test cases
for t in range(T):
    N, K = [int(v) for v in input().split()]  # total, minimum
    U = float(input())  # training units
    P = [float(x) for x in input().split()]  # probabilities
    P.sort()

    prob = 0.0
    if N == 1:
        # increase at maximum
        prob = P[0] + U
    elif N == K:
        # small 1
        # check if arrive to 1.0
        if U == N - np.sum(P):
            prob = 1.0
        else:
            # increase the smaller ones
            finished = False
            idsec = 1
            while not finished:
                if P[idsec] - P[0] > 0:
                    num = idsec
                    tospend = P[idsec] - P[0]
                    if tospend * num <= U:
                        U -= tospend * num
                    else:
                        tospend = U / num
                        U = 0
                        finished = True
                    # spend the learning
                    for i in range(idsec):
                        P[i] += tospend

                # increase the small index
                idsec += 1
                if idsec == N:
                    finished = True
            # Spend remaining U overall
            if U > 0:
                tospend = U / N
                for i in range(N):
                    P[i] += tospend
            # Final value
            prob = 1.0
            for i in range(N):
                    prob *= P[i]

    print("Case #{:d}: {:.8f}".format(t + 1, prob))
