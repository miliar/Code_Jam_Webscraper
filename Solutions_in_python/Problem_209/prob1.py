import sys
import glob, os

def solve_file(filen):
    f = open(filen + '.in', 'r')
    T = int(f.readline())

    ans = ""

    for i in range(1, T+1):
        line = f.readline().split(" ")

        N = int(line[0])
        K = int(line[1])
        R = [];
        H = [];

        for j in range(N):
            line = f.readline().split(" ")
            R.append(float(line[0]))
            H.append(float(line[1]))

        nans = solve_cks(N, K, R, H)

        ans += "Case #%d: %s\n" % (i, nans)

    f = open(filen + '.out', 'w')
    f.write(ans)
    print(ans)

def solve_cks(N, K, R, H):
    Rus = reversed(sorted(list(set(R))))
    SA = []
    for i in range(N):
        SA.append(2 * 3.141592 * R[i] * H[i])

    ansMax = 0
    for r in Rus:
        print(r)
        Rst = []
        Hst = []
        SAst = []
        hb = 0
        bind = 0

        for i in range(N):
            if R[i] <= r:
                Rst.append(R[i])
                Hst.append(H[i])
                SAst.append(SA[i])
            if R[i] == r:
                if SA[i] > hb:
                    hb = SA[i]
                    bind = len(Rst) - 1

        if len(Rst) < K:
            break

        SAst.pop(bind)
        Rst.pop(bind)
        Hst.pop(bind)

        SAs = list(reversed(sorted(SAst)))
        print(SAs)
        SAm = sum(SAs[0:K-1])+hb
        ans = SAm + r**2*3.141592
        print(hb)
        print(ans)

        if ans > ansMax:
            ansMax = ans

    return ansMax

if __name__ == '__main__':

    for file in glob.glob("*.in"):
        filen = file[0:-3]
        print(filen)
        solve_file(filen)