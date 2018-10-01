from __future__ import division

def groupLines(inlines, count):
    lines = []
    for line in inlines:
        lines.append(line.strip())
        if len(lines) >= count:
            yield lines
            inlines.readline() #discard the pointless blank line in the data (why is it even there?)
            lines = []

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
        outputs = pool.map(processor, groupLines(inf, 4))
        for i, result in enumerate(outputs, 1):
            string = "Case #%s: %s" % (i, result)
            if i > 1:
                outf.write("\n")
            outf.write(string)

    solve(inPath, processor, outDir)

def processor(board):
    #initialising: could minimise redundancy by building all off teamNames
    #but minimal payout (unless we wanted to make arbitrary player tic-tac-toe-tomek)
    teamNames = {1:"O", 2:"X"}
    teams = {".":0, "T":(1 | 2), "O":1, "X":2}
    teamsBoard = [[teams[cell] for cell in row] for row in board]
    for team in (1, 2):
        for line in boardLines():
            if all((teamsBoard[x][y] & team) > 0 for x, y in line): #found a winning line
                return "{} won".format(teamNames[team])
    if all(all(cell > 0 for cell in row) for row in teamsBoard):
        return "Draw"
    else:
        return "Game has not completed"

def boardLines(size = 4):
    for row in range(size):
        yield ((x, row) for x in range(size))
    for column in range(size):
        yield ((column, y) for y in range(size))
    yield ((d, d) for d in range(size))
    yield ((d, size - 1 - d) for d in range(size))

