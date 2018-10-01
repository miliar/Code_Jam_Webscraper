import sys


def time_to_finish(X, cookies_rate):
    """Returns required time to reach X at cookies_rate cookies per seconds"""
    return X/cookies_rate

def time_to_buy(C, cookies_rate):
    """Returns required time to buy a factory (cost=C) at cookies_rate cookies per seconds"""
    return C/cookies_rate

def solve(t):
    C, F, X = (float(x) for x in sys.stdin.readline().rstrip().split())
    cookies_rate = 2
    cur_time = 0
    cur_to_finish = time_to_finish(X, cookies_rate)
    prev_to_finish = cur_to_finish + 1
    while cur_to_finish < prev_to_finish:
        prev_to_finish = cur_to_finish
        cur_time += time_to_buy(C, cookies_rate)
        cookies_rate += F
        cur_to_finish = cur_time + time_to_finish(X, cookies_rate)

    sys.stdout.write("Case #%i: %.7f\n" % (t, prev_to_finish))


T = int(sys.stdin.readline())
for t in range(1, T+1):
    solve(t)
