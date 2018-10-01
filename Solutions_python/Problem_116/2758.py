def check(grid):
    for i in xrange(4):
        if check_line(grid[i]):
            c = grid[i][0]
            if c == 'T':
                c = grid[i][1]
            return c + " won"

        if check_line([grid[j][i] for j in xrange(4)]):
            c = grid[0][i]
            if c == 'T':
                c = grid[1][0]
            return c + " won"

    if check_line([grid[i][i] for i in xrange(4)]):
        c = grid[0][0]
        if c == 'T':
            c = grid[1][0]
        return c + " won"

    if check_line([grid[i][3-i] for i in xrange(4)]):
        c = grid[0][3]
        if c == 'T':
            c = grid[1][0]
        return c + " won"

    return ("Game has not completed"
            if '.' in grid[0]
            or '.' in grid[1]
            or '.' in grid[2]
            or '.' in grid[3]
            else "Draw")

def check_line(line):
    char = line[0]
    if char == 'T':
        char = line[1]
    for i in xrange(1, 4):
        c = line[i]
        if c == '.' or (c != char and c != 'T'):
            break
        if i == 3:
            return True
    return False

num_cases = int(raw_input())
for case in xrange(num_cases):
    grid = [raw_input() for _ in xrange(4)]
    raw_input() # skip newline
    print "Case #%d: %s" % (case + 1, check(grid))
