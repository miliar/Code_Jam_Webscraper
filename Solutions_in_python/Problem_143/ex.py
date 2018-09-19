import sys


def main():
    with open(sys.argv[1]) as f:
        f.readline()  # number of cases, redundant
        lines = f.read().splitlines()
    for i, l in enumerate(lines, start=1):
        a, b, k = (int(x) for x in l.split())
        ans = solve(a, b, k)
        print('Case #{}: {}'.format(i, ans))


def solve(a, b, k):
    chances = 0
    for machine_a in range(a):
        for machine_b in range(b):
            if machine_a & machine_b < k:  # bitwise and
                chances += 1
    return chances

assert solve(3, 4, 2) == 10

if __name__ == '__main__':
    main()