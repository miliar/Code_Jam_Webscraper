def solve(N, R, O, Y, G, B, V):
    Color = [('R', R), ('Y', Y), ('B', B)]
    if R > N/2 or Y > N/2 or B > N/2: return 'IMPOSSIBLE'
    Color = sorted(Color, key=lambda x: x[1], reverse=True)
    res = [Color[0][0], 0, 0] * Color[0][1]
    len_res = Color[0][1]
    for i in range(Color[1][1]):
        res[3 * (len_res - i - 1) + 2] = Color[1][0]
    for i in range(Color[2][1]):
        res[3 * i + 1] = Color[2][0]
    return ''.join(filter(lambda x: x != 0, res))

T = input()
for t in range(1, T + 1):
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    print 'Case #%d: %s'%(t, solve(N, R, O, Y, G, B, V))
