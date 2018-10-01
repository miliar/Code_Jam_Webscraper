INPUT = {
    'dimensions': ('int', 'linearray'),
    'input_grid': ('string', ('constant', lambda x: x['dimensions'][0]))
}

INPUT_ORDER = ['dimensions', 'input_grid']

TEST = ('''\
3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..
''','''\
Case #1:
Impossible
Case #2:
.
Case #3:
./\..
.\//\\
./\\\/
.\/..
''')

SEPARATOR = '\n'

def main(dimensions, input_grid):
    # parse grid
    grid = []
    blues = 0
    for x in range(dimensions[0]):
        grid.append([])
        for y in range(dimensions[1]):
            if input_grid[x][y] == '.':
                grid[x].append(0)
            else:
                grid[x].append(1)
                blues = blues + 1
    # give up if number of blue tiles in not divisible by 4
    if blues & 3: return "Impossible"
    
    def coverable(i,j):
        return 1 == (grid[i][j] & grid[i][j+1] & grid[i+1][j] & grid[i+1][j+1])
        
    def cover(i,j):
        grid[i][j] = '/'
        grid[i][j+1] = '\\'
        grid[i+1][j] = '\\'
        grid[i+1][j+1] = '/'
    
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            if grid[x][y] == 1:
                if coverable(x,y):
                    cover(x,y)
                else:
                    return 'Impossible'
                
    # convert back white tiles
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            if grid[x][y] == 0:
                grid[x][y] = '.'
    return '\n'.join([''.join(l) for l in grid])