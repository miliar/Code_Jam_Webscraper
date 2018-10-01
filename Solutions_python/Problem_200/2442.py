#!/usr/env/bin python3
import sys

numbers = []
with open(sys.argv[1]) as f:
    T = int(f.readline())
    for line in f.readlines():
        numbers += [[int(x) for x in line.strip()]]

def calc(nr):
    for i in range(len(nr) - 1, 0, -1):
        if nr[i - 1] > nr[i]:
            nr[i - 1] = nr[i - 1] - 1
            for j in range(i, len(nr)):
                nr[j] = 9
    return nr


for t in range(T):
    out = "Case #{}: ".format(t + 1)
    result = int("".join([str(i) for i in calc(numbers[t])]))
    out += str(result)
    print(out)
