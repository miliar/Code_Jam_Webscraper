"""
Google Code Jam

Author  : ChesterAiGo
Language: Python 3
"""

################################################### SOLUTION
def init():
    pass

def column(matrix, i):
    return [row[i] for row in matrix]

def solve(input):
    row = input[0]
    col = input[1]
    grid = input[2]
    isFull = True

    for l in grid:
        if('?' in l):
            isFull = False
            break

    if(isFull):
        return grid

    newGrid = []

    grid = [list(line) for line in grid]

    for x in range(row):
        tempChar = '?'
        for y in range(col):
            if(grid[x][y] != '?'):
                tempChar = grid[x][y]
            else:
                grid[x][y] = tempChar


    for x in range(row):
        tempChar = '?'
        for y in range(col - 1, -1, -1):
            if(grid[x][y] != '?'):
                tempChar = grid[x][y]
            else:
                grid[x][y] = tempChar

    # print(grid)

    for x in range(row):
        for y in range(col):
            if(grid[x][y] == '?'):
                tempChar = '?'
                for i in column(grid, y)[x+1:row+1:1]:
                    if(i != '?'):
                        tempChar = i
                        break

                if(tempChar == '?'):
                    for i in column(grid, y)[:x][::-1]:
                        if(i != '?'):
                            tempChar = i
                            break

                grid[x][y] = tempChar


    return [''.join(line) for line in grid]

#################################################### HELPERS

def readOneTc():
    # FOR 1 2 3
    # tc = [int(x) for x in input().split(" ")]
    #
    # FOR A B C
    # tc = [x for x in input().split(" ")]
    #
    # FOR ABCD
    # tc = input()
    #
    # FOR 3
    #      0 0 0
    # tc_n = int(input())
    # tc_l = [int(x) for x in input().split(" ")]
    # tc = (tc_n, tc_l)
    #
    # FOR 2
    #     0 1
    #     9 8
    temp = input()
    tc_row = int(temp.split(" ")[0])
    tc_col = int(temp.split(" ")[1])
    tc_l = []

    for i in range(tc_row):
        tc_l.append(input())

    tc = (tc_row, tc_col, tc_l)

    return tc


# For testing
# print("Answer: ")
# temp = solve(readOneTc())
# for line in temp:
#     print(line)

# print([0,1,2,10][1:4])
# print([0,1,2,3][:1])

# print([l for l in range(9, -1, -1)])
# print(set("GC"))

# For processing all
for case_number in range(1, 101):
    temp = solve(readOneTc())
    print("Case #{0}: ".format(str(case_number)))

    for line in temp:
        print(line)

