def time_taken(d, horse):
    pos, spd = horse
    return (d - pos) / spd


def solve(d, horses):
    max_time = max(time_taken(d, horse) for horse in horses)
    return d / max_time


def main():
    t_case = int(input())
    for i in range(t_case):
        d, n = map(int, input().split())
        horses = [tuple(map(int, input().split()))
                  for _ in range(n)]
        print("Case #{}: {:0.6f}".format(i + 1, solve(d, horses)))


if __name__ == "__main__":
    import sys

    sys.stdin = open("A-large.in", "r")
    sys.stdout = open("out", "w")
    main()
