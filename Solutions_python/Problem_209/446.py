from math import pi

def parse():
    n, k = map(int, input().split())
    pancakes = []
    for _ in range(n):
        pancakes.append(tuple(map(int, input().split())))
    return n, k, pancakes

def area(pcks):
    biggest = max(pcks, key=lambda x: x[0])
    heights = [x[1] for x in pcks]

    return pi * biggest[0] * biggest[0] + 2 * pi * sum(x[0] * x[1] for x in pcks)

def solve(n, k, pancakes):
    biggest = max(pancakes, key=lambda x: (x[0], -x[1]))
    k_by_thickness = list(reversed(sorted(pancakes, key=lambda x: x[0] * x[1])))[0:k]

    try_area = 0
    if biggest not in k_by_thickness:
        k_minus_one = k_by_thickness[0:k - 1]
        k_minus_one.append(biggest)
        try_area = area(k_minus_one)

    ans = max(area(k_by_thickness), try_area)
    print('{0:.6f}'.format(ans))

t = int(input())
for tc in range(t):
    print("Case #" + str(tc + 1) + ":", end=' ')
    solve(*parse())