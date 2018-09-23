def get_l_diag(grid, l):
    n = len(grid)
    ll = []
    for r in range(len(grid)):
        for c in range(len(grid)):
            if r + (n - c - 1) == l:
                ll.append(grid[r][c])
    return ll

def get_r_diag(grid, l):
    n = len(grid)
    ll = []
    for r in range(len(grid)):
        for c in range(len(grid)):
            if r + c == l:
                ll.append(grid[r][c])
    return ll

def get_cols(grid):
    ll = []
    for c in range(len(grid)):
        col = []
        for r in range(len(grid)):
            col.append(grid[r][c])
        ll.append(col)
    return ll

def is_grid_valid(grid):
    # check rows
    for row in grid:
        x_c = row.count('x')
        o_c = row.count('o')
        r_c = row.count('+')
        if x_c + o_c > 1:
            return False
    # check cols
    for col in get_cols(grid):
        x_c = col.count('x')
        o_c = col.count('o')
        r_c = col.count('+')
        if x_c + o_c > 1:
            return False
    # check left diags
    for i in range(2 * len(grid) - 1):
        l_diag = get_l_diag(grid, i)
        x_c = l_diag.count('x')
        o_c = l_diag.count('o')
        r_c = l_diag.count('+')
        if o_c + r_c > 1:
            return False
    # check right diags
    for i in range(2 * len(grid) - 1):
        r_diag = get_r_diag(grid, i)
        x_c = r_diag.count('x')
        o_c = r_diag.count('o')
        r_c = r_diag.count('+')
        if o_c + r_c > 1:
            return False
    return True

def recur_grid(grid, r, c, moves):
    n = len(grid)
    if not is_grid_valid(grid):
        return (-1, moves)
#    print grid
    if c == n:
        return recur_grid(grid, r+1, 0, moves)
    if r == n:
        return (score_grid(grid), moves)
    k = grid[r][c]
    best_score = -1
    best_moves = []
    if k == '.':
        grid[r][c] = '+'
        moves.append(('+', r, c))
        score_tuple = recur_grid(grid, r, c+1, moves)
        if score_tuple[0] > best_score:
            best_score = score_tuple[0]
            best_moves = list(score_tuple[1])
        moves.pop()
        grid[r][c] = 'x'
        moves.append(('x', r, c))
        score_tuple = recur_grid(grid, r, c+1, moves)
        if score_tuple[0] > best_score:
            best_score = score_tuple[0]
            best_moves = list(score_tuple[1])
        moves.pop()
        grid[r][c] = k
    elif k == '+' or k == 'x':
        grid[r][c] = 'o'
        moves.append(('o', r, c))
        score_tuple = recur_grid(grid, r, c+1, moves)
        if score_tuple[0] > best_score:
            best_score = score_tuple[0]
            best_moves = list(score_tuple[1])
        moves.pop()
    score_tuple = recur_grid(grid, r, c+1, moves)
    if score_tuple[0] > best_score:
        best_score = score_tuple[0]
        best_moves = list(score_tuple[1])
    return (best_score, best_moves)

def score_grid(grid):
    total = 0
    if not is_grid_valid(grid):
        return -1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            k = grid[r][c]
            if k == 'o':
                total += 2
            elif k == '.':
                pass
            else:
                total += 1
    return total

def get_bottom(grid):
    moves = []
    n = len(grid)
    for c in range(1, n - 1):
        if grid[n -1][c] == '.':
            grid[n-1][c] = '+'
            moves.append(('+', n-1, c))
    return moves

def populate_diags(grid):
    bad_col = grid[0].index('o')
    moves = []
    row = 1
    n = len(grid)
    inc = 1
    if bad_col > n/2:
        inc = -1
        row = n - 1
    for c in range(n):
        if c == bad_col:
            continue
        moves.append(('x', row, c))
        grid[row][c] = 'x'
        row += inc
    return moves

def populate_top(grid):
    moves = []
    n = len(grid)
    for c in range(n):
        if grid[0][c] == '.':
            grid[0][c] = '+'
            moves.append(('+', 0, c))
    return moves

def convert_top_row(grid):
    moves = []
    n = len(grid)
    for c in range(n):
        if grid[0][c] == 'o':
            return moves
    for c in range(n):
        if grid[0][c] == 'x':
            grid[0][c] = 'o'
            moves.append(('o', 0, c))
            return moves
    for c in range(n):
        if grid[0][c] == '.':
            grid[0][c] = 'o'
            moves.append(('o', 0, c))
            return moves
    for c in range(n):
        if grid[0][c] == '+':
            grid[0][c] = 'o'
            moves.append(('o', 0, c))
            return moves
    return []

t = input()

def pretty_print(grid):
    for line in grid:
        print ''.join(line)

def solve_small(grid):
    moves = []
    moves.extend(convert_top_row(grid))
    moves.extend(populate_top(grid))
#    pretty_print(grid)
#    return recur_grid(grid, 1, 0, moves)
    moves.extend(populate_diags(grid))
    moves.extend(get_bottom(grid))
    return (score_grid(grid), moves)

for i in range(1, t+1):
    n, m = map(int, raw_input().strip().split())
    grid = []
    for _ in range(n):
        grid.append(['.'] * n)
    for _ in range(m):
        k, r, c = raw_input().strip().split()
        r = int(r)
        c = int(c)
        r -= 1
        c -= 1
        grid[r][c] = k
    score, moves = solve_small(grid)
    print 'Case #{}: {} {}'.format(i, score, len(moves))
#    for k, r, c in moves:
#        print '{} {} {}'.format(k, r+1, c+1)
#    pretty_print(grid)
