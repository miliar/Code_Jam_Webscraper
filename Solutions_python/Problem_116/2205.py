with open("A-large.in") as f:
    n = int(f.readline().rstrip())
    
    def readCase(caseLines):
        c = [["A","B","C","D"] for i in range(4)]
        for i in range(4):
            line = caseLines[i]
            for j in range(4):
                c[i][j] = line[j]
        return c
    
    def evalCase(case):
        def conv(char):
            if char == 'O':
                return -1
            elif char == 'T':
                return 0
            elif char == 'X':
                return 1
            elif char == '.':
                return 0.05
        completed = True

        def check(line):
            rowSum = sum(list(map(conv, line)))
            if rowSum in [3,4]:
                return "X won"
            if rowSum in [-3,-4]:
                return "O won"
            else:
                return None

        for row in case:
            res = check(row)
            if res:
                return res
            if '.' in row:
                completed = False

        cols = map(list, zip(*case))
        for col in cols:
            res = check(col)
            if res:
                return res
            if '.' in col:
                completed = False

        diag1 = [case[i][i] for i in range(4)]
        diag2 = [case[i][3-i] for i in range(4)]

        res = check(diag1)
        if res:
            return res
        res = check(diag2)
        if res:
            return res

        if not completed:
            return "Game has not completed"
        else:
            return "Draw"

    def readLines(f, n):
        ll = [f.readline().rstrip() for i in range(n)]
        f.readline() # read newline
        return ll

    for i in range(n):
        c = readCase(readLines(f, 4))
        print("Case #%i: %s" % (i+1, evalCase(c)))
