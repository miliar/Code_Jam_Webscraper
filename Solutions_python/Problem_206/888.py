#!/usr/bin/env python3

num_cases = int(input())

for case in range(1, num_cases+1):
    dest, num_horses = map(int, input().split())

    horses = [tuple(map(int, input().split())) for i in range(num_horses)]

    hours = max((dest - pos) / speed for pos, speed in horses)

    cruising_speed = dest / hours

    print("Case #{case}: {answer:.6f}".format(case=case, answer=cruising_speed))
