err = 0.000000000001
RATE = 0
T = 1
def solve(N, V, X, S):
    """ solve the problem """

    #print(N, V, X, S)
    if N == 1:
        s = S[0]
        rate = s[RATE]
        t = s[T]
        if t- err < X < t+err:
            return V / rate
        else:
            return 'IMPOSSIBLE'

    if N == 2:
        ans1 = 0
        ans2 = 0
        ans = 0
        s1 = S[0]
        s2 = S[1]
        rate1 = s1[RATE]
        rate2 = s2[RATE]
        t1 = s1[T]
        t2 = s2[T]
        if not (min(t1,t2)-err < X < max(t1, t2)+err):
            return 'IMPOSSIBLE'

        if (t1-err < X < t1+err) and (t2-err < X < t2+err):
            return V / (rate1+rate2)
        if t1- err < X < t1+err:
            return V / rate1
        if t2- err < X < t2+err:
            return V / rate2

        if t1 < t2:
            t1, t2 = t2, t1
            rate1, rate2 = rate2, rate1

        #print('ere', t1, )
        a = V / (t1-t2)
        #time1 = a * (X-t2) / rate1
        #time2 = a * (t1-X) / rate2
        time1 = (V * (X-t2)) / (rate1 * (t1-t2))
        time2 = (V * (t1-X)) / (rate2 * (t1-t2))

        return max(time1, time2)

    return 


def parse():
    """ parse input """

    N, V, X = [i for i in input().split()]
    N = int(N)
    V = float(V)
    X = float(X)
    S = []
    for i in range(N):
        S.append([float(_) for _ in input().split()])

    return N, V, X, S


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        if result == 'IMPOSSIBLE':
            print('Case #%d: %s' % (t, result))
        else:
            print('Case #%d: %.10f' % (t, result))


if __name__ == '__main__':

    main()
