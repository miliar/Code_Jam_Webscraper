def world_cup(P, M, prices):
    N = 2**P
    M = [P-i for i in M]
    amount = 0
    for r in range(P, 0, -1):
        m = 2**r
        needed = set()
        for i in range(N):
            if M[i] > 0:
                needed.add(i/m)
                M[i] -= 1
        for index in needed:
            amount += prices[r-1][index]
    return amount

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        P = int(raw_input())
        M = [int(s) for s in raw_input().strip().split(' ')]
        prices = []
        for p in range(P):
            prices.append([int(s) for s in raw_input().strip().split(' ')])
        print 'Case #%d: %d' % (t+1, world_cup(P, M, prices))
