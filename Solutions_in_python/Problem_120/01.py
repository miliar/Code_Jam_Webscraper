# pi * ((r + 1) ** 2 - r ** 2)
# pi * (r + 1 - r) * (r + 1 + r)
# pi * (2 * r + 1) => (2 * r + 1) ml
# sum(2 * k + 1, k=r..+inf step 2)
# (2 * r + 1) + (2 * r + 4 + 1) + (2 * r + 8 + 1) + ...
# (2 * r + 1) * n + arith-progression(start=0, step=4, n)
# sum of progression = (n - 1) * n * 4 / 2
# t >= (2 * r + 1) * x + x * (x - 1) * 2
# t >= x * (2 * r + 2 * x - 1)
from math import floor, sqrt


for i in range(int(input())):
    r, t = tuple(map(int, input().split()))
    D = 1 - 2 * ((2 * r + 1) - t)
    x = floor((sqrt(4 * r * (r - 1) + 8 * t + 1) - 2 * r + 1) / 4)
    while t < x * (2 * r + 2 * x - 1):
        x = x - 1
    print("Case #{}: {}".format(i + 1, x))
