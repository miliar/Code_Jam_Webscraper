##row = [None for x in range(R)]
##col = [None for y in range(C)]
filename = "A-large.in"
infile = open(filename, 'r')
lines = infile.readlines()

cases = []
t = int(lines[0].strip('\n'))
for line in lines:
    cases.append(str(line).strip('\n'))

infile.close()






##R = 5
##C = 10
##
##
##
##
##for i in range(len(grid)):
##    row = grid[i]
##
##    for j in range(len(row)):
##        row[j] = line[i][j]
grids = []
for i in range(len(cases)):
    case = cases[i]
    RC = case.split(' ')
    if len(case.split(' ')) == 2:
        count = 0
        R = int(RC[0])
        C = int(RC[1])
        print (R,C)
        grid = [[None for x in range(C)] for y in range(R)]
        for j in range(i+1, R+i+1):
            print(cases[j])
            for k in range(len(cases[j])):
                grid[count][k] = cases[j][k]
            count+=1
        
        grids.append(grid)

#for each letter find the furtherst, if found then duplicated until there
#if not found then pass first


def findFar(grid):
    while not isCut(grid):
        useVert = isRowEmpty(grid)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                element = grid[y][x]
                if element is not '?':
##                    xx,yy = findEle(grid,element)
##                    if len(xx) > 1:
##                        grid = diag(xx[0],yy[0],xx[-1],yy[-1],element,grid)
##                    else:
##                        #duplicate horizontally
                    if useVert:
                        grid = vert(x,y,element,grid)
                    else:
                        grid = hori(x,y,element,grid)

    return grid
                    
def findEle(grid,e):
    xx = []
    yy = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == e:
                xx = xx + [x]
                yy = yy + [y]

    return (xx,yy)

def hori(x,y,e,grid): #y increases
    changed = False
    for i in range(len(grid[y])):
        if grid[y][i] is '?':
            changed = True
            grid[y][i] = e
        else:
            if changed == True and grid[y][i] is not e:
                break
            if i > x:
                break
    return grid

def vert(x,y,e,grid):
    changed = False
    rowI = 0
    for row in grid:
        if row[x] == '?':
            changed = True
            row[x] = e
        else:
            if changed == True and row[x] is not e:
                break
            if rowI>y:
                break
        rowI+=1
    return grid
def diag(x1,y1,x2,y2,e,grid):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            grid[y][x] = e

    return grid

def isRowEmpty(grid):
    for row in grid:
        empty = True
        for element in row:
            if element is not '?':
                empty = False
        if empty:
            return True
    
    return False
def printGrid(grid):
    result = []
    for row in grid:
        r = ''
        for element in row:
            r += element
        r+='\n'
        print(r,end='')
        result.append(r)
    return result
def isCut(grid):
    for row in grid:
        r = ''
        for element in row:
            if element == '?':
                return False
        
    return True


outfile = open("A-large.out", 'w')

caseNo = 1
for grid in grids:
    grid = findFar(grid)
    outfile.write("Case #{}:\n".format(caseNo))
    for r in printGrid(grid):
        outfile.write(r)
    caseNo += 1

outfile.close()
