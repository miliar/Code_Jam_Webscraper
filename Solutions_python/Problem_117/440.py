string = [s.strip() for s in
          open('input2.txt').readlines()[1:] if len(s.strip())]


def get_chunk():
    res = []
    for index, line in enumerate(string):
        if not res:
            Y, X = [int(x) for x in line.split(' ')]
        res.append([int(x) for x in line.split(' ')])
        if len(res) == Y + 1:
            yield res[1:]
            res = []

    if res:
        yield res


def solve(chunk):
    Y = len(chunk)
    X = len(chunk[0])
    rows_max = [0] * Y
    cols_max = [0] * X
    for i in xrange(Y):
        rows_max[i] = max(chunk[i])
    for i in xrange(X):
        vmax = 0
        for j in xrange(Y):
            if chunk[j][i] > vmax:
                vmax = chunk[j][i]
        cols_max[i] = vmax
    # print chunk
    # print cols_max
    # print rows_max
    for i in xrange(Y):
        for j in xrange(X):
            if chunk[i][j] < cols_max[j] and chunk[i][j] < rows_max[i]:
                return 'NO'
    return 'YES'

    return 'to solve yet'

for index, chunk in enumerate(get_chunk()):
    print 'Case #%s:' % (index + 1), solve(chunk)
    # break
