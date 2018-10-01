def check(lst):
    if lst[0] == 'T':
        lst = lst[1] + lst[1] + lst[2] + lst[3]
    elif lst[1] == 'T':
        lst = lst[0] + lst[0] + lst[2] + lst[3]
    elif lst[2] == 'T':
        lst = lst[0] + lst[1] + lst[0] + lst[3]
    elif lst[3] == 'T':
        lst = lst[0] + lst[1] + lst[2] + lst[0]
    if lst[0] != '.' and lst[0] == lst[1] and lst[0] == lst[2] and lst[0] == lst[3]:
        return True
    else:
        return False


def winner(lst):
    if lst[0] == 'T':
        return lst[1]
    else:
        return lst[0]

infile = open('A-large.in', 'r')
outfile = open('output.txt', 'w')

t = int(infile.readline())

for i in xrange(t):
    line = []
    end = True
    line += [infile.readline()]
    line += [infile.readline()]
    line += [infile.readline()]
    line += [infile.readline()]
    empty = infile.readline()
    line += [line[0][0] + line[1][0] + line[2][0] + line[3][0]]
    line += [line[0][1] + line[1][1] + line[2][1] + line[3][1]]
    line += [line[0][2] + line[1][2] + line[2][2] + line[3][2]]
    line += [line[0][3] + line[1][3] + line[2][3] + line[3][3]]
    line += [line[0][0] + line[1][1] + line[2][2] + line[3][3]]
    line += [line[0][3] + line[1][2] + line[2][1] + line[3][0]]
    for j in xrange(10):
        if check(line[j]):
            end = False
            outfile.write('Case #' + str(i + 1) + ': ' + str(winner(line[j])) + ' won\n')
            break
    if end:
        for j in xrange(10):
            if '.' in line[j]:
                outfile.write('Case #' + str(i + 1) + ': Game has not completed\n')
                end = False
                break
    if end:
        outfile.write('Case #' + str(i + 1) + ': Draw\n')

outfile.close()
