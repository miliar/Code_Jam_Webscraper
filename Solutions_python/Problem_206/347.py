T = int(input())


def horse_time(k, s, d):
    diff = d - k
    tm = diff / s
    return tm


def solve_case():
    d, n = [int(x) for x in input().split()]
    horses = [[int(x) for x in input().split()] for i in range(n)]
    times = [horse_time(k, s, d) for k, s in horses]
    max_time = max(times)
    rec_speed = d / max_time
    return rec_speed


for I in range(1, T + 1):
    print("Case #{}: {}".format(I, solve_case()))   
