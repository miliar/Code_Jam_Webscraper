def solve(N, R, O, Y, G, B, V):
    # solve
    ans = ['-'] * N

    OB, N, B = solve_complements(N, O, B, 'O', 'B')
    #print 'OB: ', OB
    GR, N, R = solve_complements(N, G, R, 'G', 'R')
    #print 'GR: ', GR
    VY, N, Y = solve_complements(N, V, Y, 'V', 'Y')
    #print 'VY: ', VY

    if N == 0:
        return OB + GR + VY
    if any([x=='IMPOSSIBLE' for x in [OB, GR, VY]]):
        return 'IMPOSSIBLE'
    else:
        BRY = solve_BRY(N, B, R, Y)
        if BRY is None:
            return 'IMPOSSIBLE'
        if OB:
            BRY[BRY.index('B')] = OB
        if GR:
            BRY[BRY.index('R')] = GR
        if VY:
            BRY[BRY.index('Y')] = VY
    return ''.join(BRY)


def solve_BRY(N, B, R, Y):
    BRY_dict = {'B':B, 'R':R, 'Y':Y}
    ret = []
    last = ''
    first = ''
    for i in range(N):
        cands = [x for x in ['B', 'R', 'Y'] if x != last]
        chosen = max(cands, key=lambda x: BRY_dict[x] + 0.01*float(first==x))
        if BRY_dict[chosen] == 0:
            return None
        ret.append(chosen)
        last = chosen
        BRY_dict[last] -= 1
        if not first:
            first = chosen
    if ret[-1] == ret[0]:
        return None
    return ret


def solve_complements(N, O, B, Os, Bs):
    if O == 0:
        return '', N, B
    if O > B:
        if N == 1:
            return Os
        else:
            return 'IMPOSSIBLE', N, B
    if O == B:
        if N == O+B:
            return ''.join([Os+Bs]*O), 0, 0
        else:
            return 'IMPOSSIBLE', N, B
    else:
        newB = B-O
        OB_str = Bs + ''.join([Os+Bs]*O)
        return OB_str, N-2*O, newB


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(1, T+1):
        N, R, O, Y, G, B, V = map(int, raw_input().split())
        #sol = solve_BRY(N, B, R, Y)
        #if sol is None:
        #    sol = 'IMPOSSIBLE'
        #else:
        #    sol = ''.join(sol)
        sol = solve(N, R, O, Y, G, B, V)
        print 'Case #{}: {}'.format(t, sol)
