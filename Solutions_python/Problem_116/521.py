d = {'.' : 0, 'X' : 1, 'O' : 2, 'T' : 3}
won = {1 : 'X won', 2 : 'O won'}

def status(lines):
    l = []
    draw = True
    for line in lines:
        m = []
        for c in line:
            if c == '.':
                draw = False
            m.append(d[c])
        l.append(m)

    for i in range(4):
        matching = l[i][0]
        for j in range(1, 4):
            if not l[i][j] & matching:
                break
            elif matching == 3:
                matching = l[i][j]
        else:
            return won[matching]

    for i in range(4):
        matching = l[0][i]
        for j in range(1, 4):
            if not l[j][i] & matching:
                break
            elif matching == 3:
                matching = l[i][j]
        else:
            return won[matching]

    matching = l[0][0]
    for i in range(1, 4):
        if not l[i][i] & matching:
            break
        elif matching == 3:
            matching = l[i][i]
    else:
        return won[matching]

    matching = l[0][3]
    for i in range(1, 4):
        if not l[i][3 - i] & matching:
            break
        elif matching == 3:
            matching = l[i][3 - i]
    else:
        return won[matching]

    if draw:
        return 'Draw'
    else:
        return 'Game has not completed'

n = input()

for i in range(n):
    l = []
    for j in range(4):
        l.append(raw_input())
    raw_input()
    print('Case #{}: {}'.format(i + 1, status(l)))
