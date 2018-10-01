#!/usr/bin/env python
import sys

T = int(input())
for case in range(1, T + 1):
    C, F, X = map(float, input().split())
    speed = 2.0
    ans = X / speed
    time = 0.0
    while (time < ans):
        ans = min(ans, time + X / speed)
        time += C / speed
        speed += F
    print("Case #" + str(case) + ": " + str(ans))
