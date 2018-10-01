#!/usr/bin/env python3

from heapq import heappush, heappop

def solve_testcase(testcase_number):
    C, F, X = [float(i) for i in input().split()]

    objective = X
    farm_cost = C
    farm_bonus = F
    time = 0
    speed = 2

    heap = []
    heappush(heap, (time, speed, 0))

    while True:
        time, speed, cookies = heappop(heap)

        if cookies > 0 :
            # The end!
            break
        else:
            time_to_farm = farm_cost / speed
            time_to_objective = objective / speed

            heappush(heap, (time + time_to_farm, speed + farm_bonus, 0))
            heappush(heap, (time + time_to_objective, speed, objective))


    print('Case #{0}: {1}'.format(testcase_number, time))


def main():
    testcases = int(input())
    for t in range(testcases):
        solve_testcase(t + 1)


if __name__ == '__main__':
    main()
