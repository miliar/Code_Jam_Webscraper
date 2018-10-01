t = int(raw_input())  # read a line with a single integer

import numpy as np

for i in xrange(1, t + 1):
    string_N, string_K = [s for s in raw_input().split(" ")]
    N = int(string_N)
    K = int(string_K)
    n = np.floor(np.log2(K))
    Kprime = K - 2**n +1
    average_interval = (N+1) / (2**n) - 1
    dec_part =  average_interval - np.floor(average_interval)

    if Kprime <= dec_part*(2**n):
        interval_size = np.ceil(average_interval)
    else:
        interval_size = np.floor(average_interval)

    max_dist = int(np.ceil( (interval_size - 1) / 2.))
    min_dist = int(np.floor( (interval_size - 1) / 2.))

    print "Case #{}: {} {}".format(i, max_dist, min_dist)
  # check out .format's