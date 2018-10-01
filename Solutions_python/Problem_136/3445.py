import sys


def time_to_x_cookies(C, F, X, limit):

    cookies = 0.0
    cookies_per_second = 2.0
    factories = 0
    time_used = 0.0

    while factories < limit:
        time_to_factory = C / cookies_per_second
        time_used += time_to_factory
        cookies_per_second += F
        factories += 1
    time_to_cookie_target = X / cookies_per_second

    return time_used + time_to_cookie_target

def minimum_time(C, F, X):

    limit = 0

    # Baseline time without factories
    time_taken = time_to_x_cookies(C, F, X, 0)

    # Add factories one at a time until they start costing time.
    while True:
        limit += 1
        factory_time = time_to_x_cookies(C, F, X, limit)
        if factory_time < time_taken:
            time_taken = factory_time
        else:
            break

    return time_taken



T = int(sys.stdin.readline())
for t in range(T):

    C, F, X = [float(n) for n in sys.stdin.readline().split()]

    print "Case #{}: {:0.7f}".format(t + 1, minimum_time(C, F, X))
