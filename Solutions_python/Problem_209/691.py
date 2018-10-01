import sys
import math
import numpy as np
T = int(sys.stdin.readline())
tests = []
for i in range(T):
    N, K = sys.stdin.readline().split(" ")
    N = int(N)
    K = int(K)
    pcks = []
    for n in range(N):
        r, h = [int(x) for x in sys.stdin.readline().split(" ")]
        pcks.append((r, h))
    tests.append((K, pcks))


# def solve_pancackes(K, pcks):
#     # pcks_values = [math.pi*r**2*h for r, h in pcks]
#     rad_values = [r for r, h in pcks]
#     N = len(pcks)
#     s_pcks_idx = sorted(range(len(rad_values)), key=lambda k: rad_values[k],
#                         reverse=True)
#     m = np.zeros((K, N+1))
#     for j in range(1, N+1):
#         idx = s_pcks_idx[j-1]
#         r, h = pcks[idx]
#         m[0][j] = math.pi*r**2 + 2*math.pi*r*h
#     for i in range(1, K):
#         for j in range(i, N+1):
#             idx = s_pcks_idx[j-1]
#             r, h = pcks[idx]
#             m[i][j] = max(m[i][j-1], m[i-1][j]+2*math.pi*r*h)
#     print m
#     i = K
#     j = N
#     return max(m[K-1][:])


def solve_panckakes2(K, pcks):
    vals = [2*math.pi*r*h for r, h in pcks]
    rad_values = [r for r, h in pcks]
    s_vals_idx = sorted(range(len(vals)), key=lambda k: vals[k], reverse=True)
    s_rads_idx = sorted(range(len(rad_values)), key=lambda k: rad_values[k],
                        reverse=True)
    tmp = 0
    for r_idx, i_r in enumerate(s_rads_idx):
        m = math.pi*pcks[i_r][0]**2 + 2*math.pi*pcks[i_r][0]*pcks[i_r][1]
        # print range(idx_r+1, min(len(s_vals_idx), idx_r+K))
        nb_add = 0
        for j in s_vals_idx:
            if nb_add >= K-1:
                break
            if j == i_r:
                continue
            if s_rads_idx.index(j) < r_idx:
                continue
            m += 2*math.pi*pcks[j][0]*pcks[j][1]
            nb_add += 1
        if m > tmp:
            tmp = m
    return tmp


for nb, t in enumerate(tests):
    K, pcks = t
    res = solve_panckakes2(K, pcks)
    sys.stdout.write("Case #{}: {}\n".format(nb+1, res))
