def fillline(line):

    ls = [c for c in line]
    imin = 0
    imax = 0
    for i in range(len(ls)):
        if ls[i] == '?':
            imax += 1
        else:
            for j in range(imin,imax):
                ls[j] = ls[i]
            imin = i+1
            imax = i+1
    if imax != imin:
        for j in range(imin,imax):
            ls[j] = ls[imin-1]
    return "".join(ls)


def fillgrid(grid):

    imin = 0
    imax = 0
    for i in range(len(grid)):
        line = grid[i]
        if set(line) == {'?'}:
            imax += 1
        else:
            grid[i] = fillline(grid[i])
            for j in range(imin,imax):
                grid[j] = fillline(grid[i])
            imin = i+1
            imax = i+1
    if imax != imin:
        for j in range(imin,imax):
            grid[j] = fillline(grid[imin-1])
    return grid

def main():
    import sys
    with open(sys.argv[1]) as f:
        nums = int(f.readline())

        for i in range(nums):
            R,C = f.readline().strip().split()
            R = int(R)

            grid = []

            for j in range(R):
                temp = f.readline().strip().split(' ')
                temp = "".join(temp)
                grid.append(temp)

            result = fillgrid(grid)
            print("Case #{:d}: ".format(i+1))

            for r in result:
                print(r)

main()
