import itertools

f = open("B-large.in", 'r')

test_cases = int(f.readline())

lawnes = []

for k in range(test_cases):
    mn = f.readline()
    mn = mn.split(' ')
    (n, m) = (int(mn[0]), int(mn[1]))

    lawn = []
    for i in range(n):
        line = f.readline()
        line = line.split(' ')
        line = map(int, line)
        lawn.append(line)
    lawnes.append(lawn)

def unshared_copy(inList):
    if isinstance(inList, list):
        return list( map(unshared_copy, inList) )
    return inList

for k in range(len(lawnes)):
    lawn = lawnes[k]

    current = unshared_copy(lawn)

    solution_found = True

    while len(list(itertools.chain(*current))) > 0:
        n = len(current)
        m = len(current[0])

        minimal = 1000000
        mi = -1
        mj = -1

        for i in range(n):
            for j in range(m):
                if current[i][j] < minimal:
                    minimal = current[i][j]
                    mi = i
                    mj = j

        column_min = True
        row_min = True
        for j in range(m):
            if current[mi][j] > minimal:
                column_min = False
                break

        if column_min:
            current.pop(mi)
        else:
            for i in range(n):
                if current[i][mj] > minimal:
                    row_min = False
                    break
            if row_min:
                list(map(lambda x: x.pop(mj), current))
            else:
                solution_found = False
                current = []
    if solution_found:
        print 'Case #' + str(k + 1) + ': YES'
    else:
        print 'Case #' + str(k + 1) + ': NO'

