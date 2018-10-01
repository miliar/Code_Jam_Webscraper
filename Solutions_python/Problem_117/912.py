import sys

number = sys.stdin.readline()
test_cases = int(number)

def check(lawn, n, m):
    vert_max = [0 for i in range(n)]

    for i in range(n):
        for j in range(m):
            if lawn[i][j] > vert_max[i]:
                vert_max[i] = lawn[i][j]

    horiz_max = [0 for j in range(m)]

    for j in range(m):
        for i in range(n):
            if lawn[i][j] > horiz_max[j]:
                horiz_max[j] = lawn[i][j]

    for i in range(n):
        for j in range(m):
            if lawn[i][j] not in [vert_max[i], horiz_max[j]]:
                return  False

    return True


for test_no in range(1, test_cases + 1):
    lawn = []
    line = sys.stdin.readline().split(" ")
    n = int(line[0])
    m = int(line[1])
    for i in range(n):
        line = sys.stdin.readline().split(" ")
        for i in range(len(line)):
            line[i] = int(line[i])

        lawn.append(line)

    if check(lawn, n, m):
        print "Case #" + str(test_no) + ": YES"
    else:
        print "Case #" + str(test_no) + ": NO"


