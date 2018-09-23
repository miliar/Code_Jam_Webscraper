def solve1(N, C, M, P, B, ttt):
    print N, C, M, P, B, ttt
    ans = 0
    prom = 0
    t = [[] for _ in range(1000)]
    for i in range(M):
        t[P[i]-1].append(B[i]-1)
    trig = 1
    while trig:
        trig = 0
        mx = max([len(tt) for tt in t])
        for i in range(1000):
            if t[i] and len(t[i]) == mx:
                ans += 1
                trig = 1
                found = 0
                for j in range(1000):
                    if t[j] and i != j:
                        if t[j].count(t[i][0]) < len(t[j]):
                            t[j].remove((t[i][0]+1)%2)
                            t[i].remove(t[i][0])
                            found = 1
                            break
                        else:
                            if t[i].count((t[i][0]+1)%2):
                                t[i].remove((t[i][0]+1)%2)
                                t[j].remove(t[i][0])
                                found = 1
                                break
                if found:
                    break
                else:
                    if i > 0 and t[i].count(t[i][0]) < len(t[i]):
                        t[i].remove(1)
                        t[i].remove(0)
                        prom += 1
                        break
                    else:
                        t[i].remove(t[i][0])
        # if ttt == 41:
        #     print t
    # print t
    return ans, prom


def solve2(N, C, M, P, B, ttt):
    print N, C, M, P, B, ttt
    ans = 0
    prom = 0
    t = [[] for _ in range(1000)]
    for i in range(M):
        t[P[i]-1].append(B[i]-1)
    trig = 1
    while trig:
        trig = 0
        mx = max([len(tt) for tt in t])
        for i in range(1000):
            if t[i] and len(t[i]) == mx:
                ans += 1
                trig = 1
                found = 0
                for j in range(1000):
                    if t[j] and i != j:
                        if t[j].count(t[i][0]) < len(t[j]):
                            t[j].remove((t[i][0]+1)%2)
                            found = 1
                            break
                if found:
                    t[i].remove(t[i][0])
                    break
                else:
                    if i > 0 and t[i].count(t[i][0]) < len(t[i]):
                        t[i].remove(1)
                        t[i].remove(0)
                        prom += 1
                        break
                    else:
                        t[i].remove(t[i][0])
        # if ttt == 41:
        #     print t
    # print t
    return ans, prom


def main():
    # f_in = open('B-small-test.in')
    f_in = open('B-small-attempt6.in')
    # f_in = open('B-large.in')
    f_out = open('B-small.out', 'w')
    # f_out = open('B-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        N, C, M = [int(i) for i in f_in.readline().split()]
        P = []
        B = []
        for _ in range(M):
            p, b = [int(i) for i in f_in.readline().split()]
            P.append(p)
            B.append(b)
        s1 = solve1(N, C, M, P, B, t)
        s2 = solve2(N, C, M, P, B, t)
        s = [0, 0]
        if s1[0] < s2[0]:
            s = s1
        if s1[0] > s2[0]:
            s = s2
        if s1[0] == s2[0]:
            s[0] = s1[0]
            s[1] = min(s1[1], s2[1])
        f_out.write("Case #{}: {} {}\n".format(t+1, s[0], s[1]))
        print "Case #{}: {} {}\n".format(t+1, s[0], s[1]),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
