T = int(raw_input())

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def find_next(p):
    global next
    l, c = p
    if next[l][c] != p:
        next[l][c] = find_next(next[l][c])
    return next[l][c]

def get_code(l, c):
    global next_code
    sink = find_next((l, c))
    if not sink in code_map:
        code_map[sink] = '%c' % (next_code + 97)
        next_code += 1
    return code_map[sink]

for i in range(T):
    print 'Case #%d:' % (i+1)
    H, W = map(int, raw_input().split(' '))
    altitude = []
    next = []
    code_map = {}
    next_code = 0
    for j in range(H):
        altitude.append(map(int, raw_input().split(' ')))
    for l in range(H):
        n = []
        for c in range(W):
            menor = altitude[l][c]
            p = (l, c)
            for k in range(4):
                l1 = l + dy[k]
                c1 = c + dx[k]
                if l1<0 or c1<0 or l1>=H or c1>=W:
                    continue
                if altitude[l1][c1] < menor:
                    menor = altitude[l1][c1]
                    p = (l1, c1)
            n.append(p)
        next.append(n)

    for l in range(H):
        linha = ''
        for c in range(W):
            linha += get_code(l, c) + ' '
        print linha




    

