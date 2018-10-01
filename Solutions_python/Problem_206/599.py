from __future__ import division

# def parse_input(str_test):
#     t = str_test.split()
#     return map(int, t)


def solve(D, N, K, S):
    max_t = 0
    for Ki,Si in zip(K,S):
        t_i = (D-Ki)/Si
        max_t = max(max_t, t_i)

    V = D/max_t
    return "{0:.6f}".format(V)
