out = open("QA.out","w")

def check(l):
    xnum = l.count('X')
    onum = l.count('O')
    tnum = l.count('T')
    if xnum + tnum == 4 and xnum >= 3:
        out.write("Case #%d: X won\n" % (test+1))
        return 1
    elif onum + tnum == 4 and onum >= 3:
        out.write("Case #%d: O won\n" % (test+1))
        return 1
    return 0

tests = int(raw_input())

for test in range(tests):
    
    right = []
    while len(right) < 4:
        line = raw_input()
        if line:
            right.append(line)

    down = [[right[row][col] for row in range(4)] for col in range(4)]
    dr = [right[x][x] for x in range(4)]
    dl = [right[x][3-x] for x in range(4)]

    complete = 0

    for row in right:
        if check(row):
            complete = 1
            break

    if complete:
        continue

    for row in down:
        if check(row):
            complete = 1
            break

    if complete:
        continue

    if check(dl):
        continue
    if check(dr):
        continue

    # check for .
    for row in right:
        if '.' in row:
            out.write("Case #%d: Game has not completed\n" % (test+1))
            complete = 1
            break

    if complete:
        continue

    out.write("Case #%d: Draw\n" % (test+1))

out.close()







