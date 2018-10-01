T = int(input())
for i in range(T):
    N, R, O, Y, G, B, V = (int(n) for n in input().split())
    def impossible():
        print('Case #%s: IMPOSSIBLE' % (i + 1))
    if O == B and (R + Y + G + V) == 0:
        print('Case #%s: %s' % (i+1, 'OB' * O))
        continue
    elif G == R and (O + Y + B + V) == 0:
        print('Case #%s: %s' % (i+1, 'RG' * G))
        continue
    elif Y == V and (R + O + G + B) == 0:
        print('Case #%s: %s' % (i+1, 'YV' * Y))
        continue
    if O + G + V > 0 and 2 * (O + G + V) + 3 > N:
        impossible()
        continue
    if O > 0 and B < O + 1:
        impossible()
        continue
    elif G > 0 and R < G + 1:
        impossible()
        continue
    elif V > 0 and Y < V + 1:
        impossible()
        continue
    Bs = B - O
    Rs = R - G
    Ys = Y - V
    def possible(N, R, Y, B):
        assert N == R + Y + B
        if R > N//2 or Y > N//2 or B > N//2:
            return None
        else:
            maxnum, maxlet = max([(R, 'R'), (Y, 'Y'), (B, 'B')])
            minnum, minlet = min([(R, 'R'), (Y, 'Y'), (B, 'B')])
            mididx = [idx for idx, let in [(0, 'R'), (1 ,'Y'), (2, 'B')] if let not in [maxlet, minlet]][0]
            midnum, midlet = [(R, 'R'), (Y, 'Y'), (B, 'B')][mididx]
            sol = [''] * N
            for j in range(maxnum):
                sol[2 * j] = maxlet
            for j in range(midnum):
                idx = N - 1 - (2 * j)
                occupant = sol[idx]
                if occupant:
                    sol[idx - 1] = midlet
                else:
                    sol[idx] = midlet
            for j in range(N):
                if not sol[j]:
                    sol[j] = minlet
            return sol
    sol = possible(Bs + Rs + Ys, Rs, Ys, Bs)
    if sol is None:
        impossible()
        continue
    else:
        def bilinear_search(seq, let):
            n = len(seq)
            for i in range(n):
                if seq[i] == let:
                    return i
                elif seq[n - 1 - i] == let:
                    return n - 1 - i
        ridx = bilinear_search(sol, 'R')
        bidx = bilinear_search(sol, 'B')
        yidx = bilinear_search(sol, 'Y')
        if O:
            sol[bidx] = 'BO' * O + 'B'
        if G:
            sol[ridx] = 'RG' * G + 'R'
        if V:
            sol[yidx] = 'YV' * V + 'Y'
        for k in range(len(sol) - 1):
            assert sol[k] != sol[k+1]
        assert sol[0] != sol[-1]
        print('Case #%s: %s' % (i+1, ''.join(sol)))
