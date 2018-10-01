from __future__ import division

def grouper(iterator):
    try:
        while True:
            N, M = (int(x) for x in next(iterator).split(" "))
            lines = []
            for row in range(N):
                lines.append(next(iterator))
            yield (N, M, lines)
    except StopIteration:
        pass

def problem(inPath, outDir = ""):
    def solve(inPath, processor, outDir = ""):
        from multiprocessing import Pool
        from os import path

        inf = open(inPath, 'rU')
        stem = path.basename(inPath)
        name, extension = path.splitext(stem)
        outName = name + ".out"
        outPath = path.join(outDir, outName)
        outf = open(outPath, 'w')

        inf.readline() #discard the line which tells us how many lines of input there are
        pool = Pool()
        outputs = pool.map(processor, grouper(line.strip() for line in inf))
        for i, result in enumerate(outputs, 1):
            string = "Case #%s: %s" % (i, result)
            if i > 1:
                outf.write("\n")
            outf.write(string)

    solve(inPath, processor, outDir)

def processor(data):
    N, M, lines = data
    field = [[int(cell) for cell in row.split(" ")] for row in lines]

    return "YES" if possible(N, M, field) else "NO"

def possible(N, M, field):
    rowValues = [max(row) for row in field]
    columnValues = [max(field[row][column] for row in range(N)) for column in range(M)]
    return all(cell == rowValues[y] or cell == columnValues[x] for x, y, cell in cells(field))

def cells(field):
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            yield (x, y, cell)
