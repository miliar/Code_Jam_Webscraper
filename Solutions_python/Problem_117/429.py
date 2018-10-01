def canCut(x, y, lawn):
    maxLine = map(lambda i: max(lawn[i]), range(0, y))
    maxCol = map(lambda i: max([_[i] for _ in lawn]), range(0, x))

    for j in xrange(0, x):
        for i in xrange(0, y):
            if lawn[i][j] not in [maxLine[i], maxCol[j]]:
                return "NO"
            if lawn[i][j] > 100:
                return "NO"

    return "YES"

if __name__ == '__main__':
    size = int(raw_input())

    for i in xrange(0, size):
        y, x = [int(_) for _ in raw_input().split()]
        data = []
        for j in xrange(0, y):
            data.append([int(_) for _ in raw_input().split()])

        print "Case #" + str(i+1) + ": " + canCut(x, y, data)
