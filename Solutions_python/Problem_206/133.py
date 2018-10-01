import sys
import bisect


def arrival_time(begin, end, speed):
    return (end - begin + 0.0) / (speed + 0.0)


def answer(D, dist_speeds):
    max_time = 0.0
    for (begin, speed) in dist_speeds:
        max_time = max([max_time, arrival_time(begin, D, speed)])
    assert max_time != 0.0
    return (D + 0.0) / max_time


if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        D, N = map(int, sys.stdin.next().split(' '))
        dist_speeds = []
        for j in range(N):
            init, speed = map(int, sys.stdin.next().split(' '))
            dist_speeds.append((init, speed))
        queries.append((D, dist_speeds))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", str(round(answer(*q), 8))])

