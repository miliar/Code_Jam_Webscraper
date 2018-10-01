
def compute_time(C, F, X):
    time = 0.0
    rate = 2.0
    while X > 0:
        first_method = X / rate
        second_method = C / rate + X / (rate + F)
        if first_method <= second_method:
            X = 0
            time += first_method
        else:
            time += C / rate
            rate += F
    return time


if __name__ == '__main__':
    nb_cases = int(raw_input())
    for case in xrange(nb_cases):
        total_time = 0.
        C, F, X = [float(v) for v in raw_input().split()]
        total_time = compute_time(C, F, X)
        print "Case #%d: %.7f" % (case + 1, total_time)
