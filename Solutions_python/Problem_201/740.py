#!/usr/bin/env python

from collections import defaultdict

def solve(N, K):

    stats = defaultdict(int)

    stats[N] = 1

    while(K > 0) :
        # print(stats)
        max_n = max(list(stats.keys()))
        num_max_n = stats[max_n]
        # print(max_n, num_max_n)

        if K <= num_max_n:
            return ((max_n-1)//2, max_n//2)

        K -= num_max_n

        del stats[max_n]

        stats[(max_n-1)//2] += num_max_n
        stats[max_n//2] += num_max_n

def main():
    case_counter = 1

    T = int(input())  # read a line with a single integer

    for i in range(1, T + 1):
        
        # Read the data
        N, K = [int(s) for s in input().split(" ")]
        # print("N: ", N)
        # print("K: ", K)

        (min_s, max_s) = solve(N, K)

        print("Case #{}: {}".format(case_counter, str(max_s) + " " + str(min_s)))
        case_counter += 1


if  __name__ =='__main__':
    main()
