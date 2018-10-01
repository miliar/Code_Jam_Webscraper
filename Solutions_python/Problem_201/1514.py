from math import floor, ceil


def get_result(num, k):
    if num == k:
        return 0, 0
    if num == 2:
        return 1, 0

    if k == 1:
        if num % 2 == 0:
            return (num / 2), (num / 2) - 1
        else:
            return (num - 1) / 2, (num - 1) / 2

    num_1 = ceil((num - 1) / 2)
    num_2 = floor((num - 1) / 2)
    if k % 2 == 0:
        return get_result(num_1, ceil((k - 1) / 2))
    else:
        return get_result(num_2, floor((k - 1) / 2))


def solve():
    n, k = [int(s) for s in input().split(" ")]
    return get_result(n, k)


t = int(input())
for i in range(1, t + 1):
    result = solve()
    print("Case #{}: {} {}".format(i, int(result[0]), int(result[1])))
