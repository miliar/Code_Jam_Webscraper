import sys
import fileinput
import heapq


def solve(case):
    stalls, people = map(int, case.split())

    gaps = [-stalls]
    heapq.heapify(gaps)

    last = 0, 0
    for _ in range(people):
        available = (-heapq.heappop(gaps)) - 1

        a = available // 2
        b = a + (available % 2)

        last = a, b

        heapq.heappush(gaps, -a)
        heapq.heappush(gaps, -b)

    return max(last), min(last)


def main():
    with fileinput.input() as f:
        num_cases = f.readline()
        for index, case in enumerate(f, start=1):
            print("Case #{0}: {1[0]} {1[1]}".format(index, solve(case)))


if __name__ == "__main__":
    sys.exit(main())
