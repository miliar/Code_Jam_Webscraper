import math
import sys


def get_lr(number):
    n = number - 1
    y = int(math.ceil(n/2.0))
    z = int(math.floor(n/2.0))
    return y, z


def get_level(stall):
    return math.floor(math.log(stall, 2))


def solve(N, K):
    if K == 1:
        return get_lr(N)

    l = get_level(K)

    prev = (2 ** l) - 1
    s_count = 2 ** l

    s_sum = N - prev
    position = K - prev

    s_min = math.floor(s_sum / s_count)
    s_max = math.ceil(s_sum /s_count)
    max_count = s_sum - (s_min * s_count)

    if position <= max_count:
        value = s_max
    else:
        value = s_min
    return get_lr(value)


if __name__ == "__main__":
    filename = sys.argv[1]
    f = open(filename)
    T = int(f.readline())

    for t in range(T):
        N, K = map(int, f.readline().strip().split())
        y, z = solve(N, K)
        answer = "{} {}".format(y, z)
        print "Case #{}: {}".format(t + 1, answer)
