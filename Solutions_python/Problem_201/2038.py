fin = open('stalls.in', 'r')
fout = open('stalls.out', 'w')

T = int(fin.readline().strip())

for t in range(T):
    line = fin.readline().split()
    N = int(line[0])
    K = int(line[1])

    stalls = [1, 1]
    L = [0, 0]
    R = [0, 0]
    for i in range(N):
        stalls.insert(1, 0)
        L.insert(1, 0)
        R.insert(1, 0)

    for k in range(K):
        # compute L and R
        for s in range(1, N+1):
            l = s - 1
            r = s + 1
            while stalls[l] == 0:
                l = l - 1
            while stalls[r] == 0 :
                r = r + 1
            L[s] = s - l - 1
            R[s] = r - s - 1

        # Choose which stall
        chosen = -1
        maxmax = -1
        maxmin = -1
        for s in range(1, N+1):
            if stalls[s] == 0:
                if chosen == -1:
                    chosen = s
                if min(L[s], R[s]) > maxmin:
                    chosen = s
                    maxmin = min(L[s], R[s])
                    maxmax = max(L[s], R[s])
                elif min(L[s], R[s]) == maxmin:
                    if max(L[s], R[s]) > maxmax:
                        chosen = s
                        maxmax = max(L[s], R[s])
        stalls[chosen] = 1

    fout.write("Case #" + str(t+1) + ": " + str(maxmax) + " " + str(maxmin) + "\n")

fin.close()
fout.close()
