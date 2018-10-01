def check_case(board, dimx, dimy):
    if dimx == 1 or dimy == 1:
        return "YES"
    ymaxes = [(max([line[x]for line in board])) for x in range(dimx)]
    y = 0
    for line in board:
        xmax = max(line)
        x = 0
        for char in line:
            if char < xmax and char < ymaxes[x]:
                return "NO"
            x += 1
        y += 1
    return "YES"

file = open("input.txt", "r")
num_cases = file.readline()
count = 1
while count < num_cases:
    line = file.readline().split()
    if not line:
        break
    x = int(line[1])
    y = int(line[0])
    board = [[int(l) for l in file.readline().split()] for line in range(y)]
    print "Case #%d: %s" %(count, check_case(board, x, y))
    count += 1

    
