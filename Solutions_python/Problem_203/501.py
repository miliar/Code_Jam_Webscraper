def solve(R, C, mat):
    for y in range(R):
        last_char = None
        for x in range(C):
            if mat[y][x] != '?':
                last_char = mat[y][x]
                i = 1
                while 0 <= x - i and mat[y][x - i] == '?':
                    mat[y][x - i] = mat[y][x]
                    i += 1
        if last_char:
            x = C - 1
            while 0 <= x and mat[y][x] == '?':
                mat[y][x] = last_char
                x -= 1

    for y in range(R):
        for x in range(C):
            if mat[y][x] == '?':
                d = 1
                while True:
                    if y + d < R and mat[y + d][x] != '?':
                        c = mat[y + d][x]
                        break
                    if 0 <= y - d and mat[y - d][x] != '?':
                        c = mat[y - d][x]
                        break
                    d += 1
                mat[y][x] = c
                d = 1
                while y + d < R and mat[y + d][x] == '?':
                    mat[y + d][x] = c
                    d += 1
                d = 1
                while 0 <= y - d and mat[y - d][x] == '?':
                    mat[y - d][x] = c
                    d += 1
    print('\n'.join(''.join(mat[y]) for y in range(R)))


T = int(input())
for tc in range(T):
    R, C = map(int, input().split())
    mat = []
    for _ in range(R):
        mat.append(list(input()))
    print('Case #{}:'.format(tc + 1))
    solve(R, C, mat)
