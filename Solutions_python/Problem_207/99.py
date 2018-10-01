IMP = 'IMPOSSIBLE'

def solve(N, R, O, Y, G, B, V):
    if R + G == N:
        if R == G:
            return G * 'RG'
        else:
            return IMP
    if O + B == N:
        if O == B:
            return O * 'OB'
        else:
            return IMP
    if Y + V == N:
        if Y == V:
            return Y * 'YV'
        else:
            return IMP

    if G and R <= G:
        return IMP
    if O and B <= O:
        return IMP
    if V and Y <= V:
        return IMP

    if G:
        rs = 'R' + G * 'GR'
        r = R - G
    else:
        rs = 'R'
        r = R

    if O:
        bs = 'B' + O * 'OB'
        b = B - O
    else:
        bs = 'B'
        b = B

    if V:
        ys = 'Y' + V * 'YV'
        y = Y - V
    else:
        ys = 'Y'
        y = Y

    su = r+b+y
    if any(2*x > su for x in [r,b,y]):
        return IMP

    if r == 0:
        return (
                bs
                + ys
                + 'BY' * (b - 1)
                )
    if b == 0:
        return (
                ys
                + rs
                + 'YR' * (y - 1)
                )
    if y == 0:
        return (
                rs
                + bs
                + 'RB' * (r - 1)
                )

    rl = [rs] + (r-1) * ['R']
    bl = [bs] + (b-1) * ['B']
    yl = [ys] + (y-1) * ['Y']

    data = [rl,bl,yl]
    data.sort(key=len, reverse=True)

    res = ''
    li = 2
    while sum(map(len, data)) != 0:
        if li == 0:
            if len(data[1]) > len(data[2]):
                res += data[1].pop()
                li = 1
            else:
                res += data[2].pop()
                li = 2

        elif li == 1:
            if len(data[2]) > len(data[0]):
                res += data[2].pop()
                li = 2
            else:
                res += data[0].pop()
                li = 0

        elif li == 2:
            if len(data[0]) >= len(data[1]):
                res += data[0].pop()
                li = 0
            else:
                res += data[1].pop()
                li = 1

    return res

def read_case():
    return map(int, input().split(' '))

T = int(input())

solutions = [solve(*read_case()) for _ in range(T)]

for i, x in enumerate(solutions):
    print("Case #{}: {}". format(i+1, x))
