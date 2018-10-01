import sys


def read_int(fp=sys.stdin):
    return int(fp.readline().strip())


def read_ints(fp=sys.stdin):
    return map(int, fp.readline().strip().split())


def read_floats(fp=sys.stdin):
    return map(float, fp.readline().strip().split())


def solve():
    base_rate = 2.0
    farm_cost, farm_rate, target = read_floats()

    best = None
    farm = 0
    while True:
        rate = base_rate
        total_time = 0
        for i in range(farm):
            total_time += farm_cost / rate
            rate += farm_rate
        total_time += target / rate

        # print "With", farm, "farms:", total_time

        if best is None or total_time < best:
            best = total_time
        if best is not None and total_time > best:
            break

        farm += 1

    return best


if __name__ == "__main__":
    T = read_int()
    for t in range(1, T+1):
        print "Case #%d: %.7f" % (t, solve())
