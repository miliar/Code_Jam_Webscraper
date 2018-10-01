inputFileName = "test.in"
inputFileName = "A-small-attempt0.in"
# inputFileName = "A-small-attempt1.in"
# inputFileName = "A-small-attempt2.in"
# inputFileName = "A-small-attempt3.in"
inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"


def fill(arr, ch, x0, y0, x1, y1):
    for y in xrange(y0, y1 + 1):
        for x in xrange(x0, x1 + 1):
            arr[y][x] = ch


def calcSingleTest(f):
    line = f.readline()
    R = int(line.split()[0])
    C = int(line.split()[1])
    arr = []

    for r in xrange(R):
        line = f.readline().strip()
        arr.append(list(line))

    x0 = 0
    y0 = 0
    for y in xrange(R):
        x0 = 0
        xma = -1
        for x in xrange(1, C + 1):
            if arr[y][C - x] != '?':
                xma = C - x
                break
        if (xma == -1):
            continue
        for x in xrange(C):
            if arr[y][x] == '?':
                continue
            ch = arr[y][x]
            if x == xma:
                fill(arr, ch, x0, y0, C - 1, y)
            else:
                fill(arr, ch, x0, y0, x, y)
                x0 = x + 1
        y0 = y + 1

    if arr[R - 1][0] == '?':
        for x in xrange(C):
            for y in xrange(R - 2, -1, -1):
                if arr[y][x] != '?':
                    ch = arr[y][x]
                    for y1 in xrange(y + 1, R):
                        arr[y1][x] = ch
                    break

    return '\n' + '\n'.join(map(lambda rr: ''.join(rr), arr))


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))
