
def winner(line):
    x = line.count('X')
    o = line.count('O')
    t = line.count('T')

    if x == 4 or x + t == 4:
        return 'X'
    if o == 4 or o + t == 4:
        return 'O'
    return None

def end(c, CC):
    print 'Case #{}:'.format(CC),
    if c in ('X', 'O'):
        print c, ' won'
    if c == 'D':
        print 'Draw'
    if not c:
        print 'Game has not completed'

NN = int(raw_input())

for CC in range(NN):
    lines = []
    cols = [[] for i in range(4)]
    dims = [[], []]

    for i in range(4):
        row = list(raw_input().strip())

        lines.append(row)
    
        for i, c in enumerate(row):
            cols[i].append(c)

    if CC < NN - 1:
        raw_input()

    for i in range(4):
        dims[0].append(lines[i][i])
        dims[1].append(lines[3 - i][i])

    lines += cols
    lines += dims

    for line in lines:
        w = winner(line)

        if w:
            end(w, CC + 1)
            break;
    else:
        if all(['.' not in line for line in lines[:4]]):
            end('D', CC + 1)
        else:
            end(None, CC + 1)

