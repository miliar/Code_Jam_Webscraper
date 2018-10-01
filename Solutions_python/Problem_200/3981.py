#!/usr/bin/env python3
def adjust(badNum):
    copy = [int(i) for i in str(badNum)]

    for i in range(len(copy) - 1):
        if copy[i] > copy[i + 1]:
            copy[i] -= 1
            for j in range(i + 1,len(copy)):
                copy[j] = 9
            if copy[i] < 0:
                copy[i] = 0
                copy[i - 1] -= 1

    return int(''.join(map(str,copy)))

def isTidy(num):
    l = str(num)
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))

def solve(num):
    current = num
    while not isTidy(current):
        current = adjust(current)

    return current

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    ans = solve(n)
    print("Case #{}: {}".format(i, ans))
