#!/usr/bin/env python3
t = int(input())
for case in range(1, t + 1):
    num = list(input())
    num = [int(x) for x in num]
    for i in reversed(range(0, len(num) - 1)):
        if num[i + 1] < num[i]:
            num[i] -= 1
            for j in range(i + 1, len(num)):
                num[j] = 9
    while (num[0] == 0):
        num = num[1:]
    numStr = [str(x) for x in num]
    print("Case #{}: {}".format(case, "".join(numStr)))
