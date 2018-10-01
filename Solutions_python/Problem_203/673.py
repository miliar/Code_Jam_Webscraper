#!/usr/bin/env python3

inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def solve(G, R, C):
    positions = []
    for j in range(C):
        for i in range(R):
            if G[i][j] != '?':
                right = j
                positions.append((j, i, G[i][j]))

    left = positions[0][0]
    top = 0
    i = 0
    ps = []
    while (i < len(positions) and positions[i][0] == left):
        ps.append(positions[i])
        i += 1

    for p in ps:
        if p != (0, top, p[2]):
            positions.append((0, p[1], p[2]))
        top = p[1] + 1

    positions.sort()


    i = len(positions)-1
    ps = []
    # print("right=",right)
    # print("positions=",positions)
    while (i >=0 and positions[i][0] == right):
        ps.append(positions[i])
        i -= 1

    bottom = R-1
    for p in ps:
        if p != (C-1, bottom, p[2]):
            if p == ps[0]:
                positions.append((C-1, R-1, p[2]))
            else:
                positions.append((C-1, p[1], p[2]))

        bottom = p[1] - 1

    positions.sort()


    left = 0
    top = 0
    lastY = positions[0][0]
    lastL = 'X'
    positions.append((C-1, R-1, positions[-1][2]))
    while positions != []:
        y, x, L = positions.pop(0)

        if y != lastY:
            for i in range(top, R):
                for j in range(left, C):
                    G[i][j] = lastL
            left = lastY + 1
            top = 0

        for i in range(top, x+1):
            for j in range(left, y+1):
                G[i][j] = L

        top = x+1
        lastY = y
        lastL = L


    # for i in range(R):
    #     for j in range(C):
    #         ns = [(-1,-1), (-1,1),(1,1),(1,-1)]
    #         for x, y in ns:
    #             if i+x >= 0 and i+x <R and j+y >= 0 and j+y <C:
    #                 if G[i][j] == G[i+x][j] == G[i][j+y]:
    #                     assert(G[i+x][j+y] == G[i][j])


    return G

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        R, C  = read_ints()
        G = [list(input()) for r in range(R)]
        # print("\n".join( map(lambda l: "".join(l), G) ))
        print('Case #%d:' % t)
        print("\n".join( map(lambda l: "".join(l), solve(G, R, C)) ))
        # print()
        # print()
