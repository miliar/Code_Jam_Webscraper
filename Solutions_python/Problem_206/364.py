import sys


def solve(d, horses, case_number):
    s = float('inf')
    for hk, hs in horses:
        r = d - hk
        if r < 0:
            continue
        t = float(r) / hs
        ns = d / t
        if ns < s:
            s = ns
    print("Case #%d: %f" % (case_number, s))


def main():
    f = sys.stdin
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')

    total_cases = f.readline()
    for case_number in range(1, int(total_cases) + 1):
        d, n = map(int, f.readline().strip().split(' '))
        horses = []
        for _ in range(0, n):
            k, s = map(int, f.readline().strip().split(' '))
            horses.append((k, s))
        solve(d, horses, case_number)


if __name__ == "__main__":
    main()
