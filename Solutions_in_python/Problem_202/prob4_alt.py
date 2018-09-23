#!/usr/bin/python

def add_model(anno_grid, m, r, c):
    if m == 'x' or m == 'o':
        for y in range(N):
            anno_grid[y][c] |= 1
        for x in range(N):
            anno_grid[r][x] |= 1
    if m == '+' or m == 'o':
        i, j = r, c
        while i >= 0 and j >= 0:
            anno_grid[i][j] |= 2
            i -= 1
            j -= 1
        i, j = r, c
        while i >= 0 and j < N:
            anno_grid[i][j] |= 2
            i -= 1
            j += 1
        i, j = r, c
        while i < N and j < N:
            anno_grid[i][j] |= 2
            i += 1
            j += 1
        i, j = r, c
        while i < N and j >= 0:
            anno_grid[i][j] |= 2
            i += 1
            j -= 1

T = int(raw_input())
for t in range(T):
    N, M = map(int, raw_input().split())
    
    orig_grid = [['.' for x in range(N)] for y in range(N)]
    anno_grid = [[0 for x in range(N)] for y in range(N)]
    
    style_points = 0
    for i in range(M):
        m, r, c = raw_input().split()
        r = int(r) - 1
        c = int(c) - 1
        orig_grid[r][c] = m
        add_model(anno_grid, m, r, c)
        style_points += 2 if m == 'o' else 1
        
#         print_grid(orig_grid)
#         print_grid(anno_grid)
    
    changes = []
    
#     print_grid(orig_grid)
#     print_grid(anno_grid)
    for r in range(N):
        if r % 2 == 0:
            r /= 2
        else:
            r = N - (r + 1) / 2
        for c in range(N):
            if anno_grid[r][c] == 0:
                add_model(anno_grid, 'o', r, c)
                changes.append('o %d %d' % (r + 1, c + 1))
                style_points += 2
            elif anno_grid[r][c] == 1:
                m = 'o' if orig_grid[r][c] == 'x' else '+'
                add_model(anno_grid, m, r, c)
                changes.append('%s %d %d' % (m, r + 1, c + 1))
                style_points += 1
            elif anno_grid[r][c] == 2:
                m = 'o' if orig_grid[r][c] == '+' else 'x'
                add_model(anno_grid, m, r, c)
                changes.append('%s %d %d' % (m, r + 1, c + 1))
                style_points += 1
    
    print "Case #%d: %d %d" % (t + 1, style_points, len(changes))
    for change in changes:
        print change