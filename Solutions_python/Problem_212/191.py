""" preparing with the input """

f = open("A-large.in").readlines()
line = 0

def raw_input():
    global line
    ans = f[line].strip()
    line += 1
    return(ans)

def raw_input_ints():
    l = raw_input()
    return([int(x) for x in l.split()])

def mod_it(G, P):
    L = [g % P for g in G]
    return(L)

def count_of(G, m):
    cnt = 0
    for k in G:
        if k == m:
            cnt += 1
    return(cnt)


def solve_4(N, G):
    G = mod_it(G, 4)
    cg0 = count_of(G, 0)
    cg1 = count_of(G, 1)
    cg2 = count_of(G, 2)
    cg3 = count_of(G, 3)

    # 2
    cg13 = min(cg1, cg3)
    cg1 -= cg13
    cg3 -= cg13
    cg22 = cg2 // 2
    cg2 -= 2 * cg22

    full_max = -1
    # 3
    # there are alternatives here!
    # depending on how many of the 1's we throw in
    for cg1_used in range(cg1 + 1):
        cg112 = min(cg1_used // 2, cg2)
        cg332 = min(cg3 // 2, max(cg2 - cg112, 0))
        cg2_now = (cg2 - cg112 - cg332)
        cg1_now = (cg1 - cg112 * 2)
        cg3_now = (cg3 - cg332 * 2)
        ans = \
            cg0 + \
            cg13 + cg22 + \
            cg112 + cg332 + \
            cg2_now // 4 + cg1_now // 4 + cg3_now // 4
        # now loner modulo check
        loners = cg2_now % 4 + cg1_now % 4 + cg3_now % 4
        if loners > 0:
            ans += 1

        full_max = max(full_max, ans)

    return(full_max)

def solve(N, P, G):
    G = mod_it(G, P)
    # print(G)
    # print(P)
    cg0 = count_of(G, 0)
    cg1 = count_of(G, 1)
    cg2 = count_of(G, 2)
    if P == 2:
        return(cg0 + ((cg1 + 1) // 2))
    elif P == 3:
        simple = count_of(G, 0)
        # print("cg0", cg0)
        # print("cg1", cg1)
        # print("cg2", cg2)
        mod_12 = min(cg1, cg2)
        loners = max(cg1, cg2) - mod_12
        # print("simple", simple)
        # print("mod12", mod_12)
        # print("loners", loners)
        loner_groups = loners // 3
        ans = simple + mod_12 + loner_groups
        if loners % 3 > 0:
            ans += 1
        return(ans)
    elif P == 4:
        simple = cg0
        return(solve_4(N, G))
    else:
        return("not implemented! %d" % P)

""" implementation """

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(T):
        N, P = raw_input_ints()
        G = raw_input_ints()
        # if i != 0:
        #     continue
        ans = solve(N, P, G)
        print("Case #%d: %d" % (i + 1, ans))

