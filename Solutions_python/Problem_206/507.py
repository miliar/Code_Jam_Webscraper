import math
from collections import defaultdict


def solve(test, input, output):
    print('Solving #{}'.format(test))

    line = input.readline()
    D = int(line.split()[0])
    N = int(line.split()[1])

    max_h = -1
    for i in range(N):
        line = input.readline()
        k = int(line.split()[0])
        s = int(line.split()[1])
        dist = (D - k) / s
        if max_h == -1:
            max_h = dist
        elif dist > max_h:
            max_h = dist
        print(max_h)

    t = D / max_h

    out = 'Case #{0}: {1:.6f}'.format(test, t)
    print(out)
    output.write(out + '\n')


with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
    test_cases = int(input.readline())
    for test in range(1, test_cases + 1):
        solve(test, input, output)
