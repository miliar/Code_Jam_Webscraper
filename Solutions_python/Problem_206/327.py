def solve(D, N, K, S):
    ans = -1
    maxh = 0
    for i in range(len(K)):
        maxh = max(maxh, (D-K[i])*1.0/S[i])
    return D/maxh


def main():
    # f_in = open('A-small-test.in')
    # f_in = open('A-small-attempt0.in')
    f_in = open('A-large.in')
    # f_out = open('A-small.out', 'w')
    f_out = open('A-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        D, N = [int(i) for i in f_in.readline().split()]
        K = []
        S = []
        for _ in range(N):
            k, s = [int(i) for i in f_in.readline().split()]
            K.append(k)
            S.append(s)
        s = solve(D, N, K, S)
        f_out.write("Case #{}: {}\n".format(t+1, s))
        print "Case #{}: {}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
