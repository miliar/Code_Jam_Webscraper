def rowSee(r0, c0, grid, searchChar):
    c = c0+1;
    while (c < len(grid[0])):
        if grid[r0][c] == searchChar:
            return True;
        if grid[r0][c] == '#':
            break;
        c += 1;
    
    c = c0-1;
    while (c >= 0):
        if grid[r0][c] == searchChar:
            return True;
        if grid[r0][c] == '#':
            break;
        c -= 1;
    return False;

def colSee(r0, c0, grid, searchChar):
    r = r0+1;
    while (r < len(grid)):
        if grid[r][c0] == searchChar:
            return True;
        if grid[r][c0] == '#':
            break;
        r += 1;
    
    r = r0-1;
    while (r >= 0):
        if grid[r][c0] == searchChar:
            return True;
        if grid[r][c0] == '#':
            break;
        r -= 1;
    return False;


def ValidateGrid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (grid[r][c] == '.') and not (rowSee(r, c, grid, '-') or colSee(r, c, grid, '|')):
                return False;

            if (grid[r][c] == '-' or grid[r][c] == '|') and (rowSee(r, c, grid, '-') or colSee(r, c, grid, '|')):
                return False
    return True;


def ClearlyImpossible(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '.':
                if not (rowSee(r, c, grid, '-') or colSee(r, c, grid, '-')):
                    return True;
    return False;

def Print(grid):
    for row in grid:
        ans = '';
        for c in row:
            ans += c;
        print ans;


def Solve(grid):        
    if ValidateGrid(grid):
        print "POSSIBLE";
        Print(grid);
        return;

    for row in data:
        for ci in range(len(row)):
            if row[ci] == '-':
                row[ci] = '|';
    
    if ValidateGrid(grid):
        print "POSSIBLE";
        Print(grid);
        return;

    for row in data:
        for ci in range(len(row)):
            if row[ci] == '|':
                row[ci] = '-';    
        
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (grid[r][c] == '-'):
                if rowSee(r, c, grid, '-') or rowSee(r, c, grid, '|'):
                    grid[r][c] = '|';

    if ValidateGrid(grid):
        print "POSSIBLE";
        Print(grid);
        return;

    for row in data:
        for ci in range(len(row)):
            if row[ci] == '-':
                row[ci] = '|';    
        
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (grid[r][c] == '|'):
                if colSee(r, c, grid, '-') or colSee(r, c, grid, '|'):
                    grid[r][c] = '-';

    if ValidateGrid(grid):
        print "POSSIBLE";
        Print(grid);
        return;

    print "IMPOSSIBLE"

#    Print(grid)


T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),

    [R, C] = map(int, raw_input().split());
    data = [];
    for r in range(R):
        data.append(list(raw_input()));

    for row in data:
        for ci in range(len(row)):
            if row[ci] == '|':
                row[ci] = '-';

#    for r in range(len(data)):
#        for c in range(len(data[r])):
#            if data[r][c] == '-' and rowSee(r, c, 
#        print row;

    Solve(data);


#    print ValidateGrid(data);
#    variableBeams = [];
    

#    print "urk"
