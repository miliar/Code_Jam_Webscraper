from math import log, ceil, floor
T = int(raw_input())

for i in range(T):
    N, K = map(int, raw_input().split())
    max_lvl = floor(log(N,2))
    k_lvl = floor(log(K,2))
    spots_left = N - (2**(k_lvl) - 1)
    max_spot_width = ceil(spots_left / (2**k_lvl))
    idx = spots_left + 2**k_lvl - 2**k_lvl*max_spot_width
    if (K-2**k_lvl+1) <= idx:
        a = ceil((max_spot_width-1) / 2.0)
        b = floor((max_spot_width-1) / 2.0)
    else:
        a = ceil((max_spot_width-2) / 2.0)
        b = floor((max_spot_width-2) / 2.0)


    print "Case #{0}: {1} {2}".format(i+1, int(a), int(b))
