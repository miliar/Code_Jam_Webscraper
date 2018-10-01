import numpy as np
import time

ncases = input()

for c in xrange(ncases):
    N, K = map(int, raw_input().split())

    stalls = np.zeros(N + 2, bool)
    stalls[0] = True
    stalls[-1] = True
    n_stalls = ~stalls.copy()

    for _ in xrange(K):
        occ = np.where(stalls)[0]

        # Do partitions
        partitions = occ[1:] - occ[:-1]
        # Get the most wide
        w = np.argmax(partitions)
        s = occ[w] + partitions[w] / 2

        stalls[s] = True

    # Compute final distance
    occ = np.where(stalls)[0]
    Ls = s - occ[occ < s][-1] - 1
    Rs = occ[occ > s][0] - s - 1
    print 'Case #%d: %d %d' % (c + 1, max(Ls, Rs), min(Ls, Rs))
