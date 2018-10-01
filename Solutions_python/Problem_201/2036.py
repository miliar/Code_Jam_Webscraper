def compute_L(stalls):
    L = []
    dist = 0
    for stall in stalls:
        if stall == 1:
            dist = -1
        L.append(dist)
        dist += 1
    return L

def compute_R(stalls):
    R = compute_L(reversed(stalls))
    R.reverse()
    return R
def choice(stalls):
    L = compute_L(stalls)
    R = compute_R(stalls)
    max_val = -1
    max_val2 = -1
    pos_max = -1
    pos_min = -1
    idx = 0
    for stall in stalls:
        x = min(L[idx], R[idx])
        y = max(L[idx], R[idx])
        if stall == 0:
            if x > max_val:
                max_val = x
                pos = idx
                max_val2 = y
            elif x == max_val and y > max_val2:
                max_val2 = y
                pos = idx
        idx += 1
    return pos

def solve(N, K):
    stalls = [0 for _ in range(N + 2)]
    stalls[0] = stalls[N + 1] = 1
    Y = Z = 0
    for S in range(K):
        S = choice(stalls)
        L = compute_L(stalls)
        R = compute_R(stalls)
        Y = max(L[S], R[S])
        Z = min(L[S], R[S])
        stalls[S] = 1
    return Y, Z

with open("C-small-1-attempt0.in") as ifile, open("stalls.out","w") as ofile:
    T = int(ifile.readline().strip())
    for testnum in range(T):
        ofile.write("Case #{}: ".format(testnum + 1))
        NK = ifile.readline().strip().split(" ")
        N, K = int(NK[0]), int(NK[1])
        Y, Z = solve(N, K)
        ofile.write("{} {}\n".format(Y, Z))
# with open ("stalls_test.txt", "w") as ofile:
#     N = 34
#     for K in range(N - 1):
#         print(K + 1)
#         Y, Z = solve(N, K + 1)
#         ofile.write("{} {}\n".format(Y, Z))
#     ofile.write("{}\n".format(N))
