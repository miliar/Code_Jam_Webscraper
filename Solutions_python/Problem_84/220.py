T = int(input())
for tc in range(1, T + 1):
    [R, C] = [int(x) for x in input().split(' ')]
    tiles = []
    for r in range(0, R):
        tiles.append(list(input()))
    print('Case #{}:'.format(tc))
    for r in range(0, R - 1):
        for c in range(0, C - 1):
            if tiles[r][c] == '#':
                if tiles[r][c + 1] == '#' and tiles[r + 1][c] == '#' and tiles[r + 1][c + 1] == '#':
                    tiles[r][c] = '/'
                    tiles[r][c + 1] = '\\'
                    tiles[r + 1][c] = '\\'
                    tiles[r + 1][c + 1] = '/'
    possible = True
    for r in range(0, R):
        if possible:
            for c in range(0, C):
                if tiles[r][c] == '#':
                    possible = False
                    break
    if not possible:
        print('Impossible')
    else:
        for r in range(0, R):
            print(''.join(tiles[r]))
