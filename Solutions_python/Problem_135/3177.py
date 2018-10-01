import sys

def readline():
    return sys.stdin.readline().strip()

def readint():
    return map(int, readline().split(" "))

cases = readint()[0]


for case in range(cases):
    guess = None
    answers = []
    for _ in range(2):
        answer = readint()[0]
        grid = []
        for _ in range(4):
            grid.append(readint())
        answers.append((answer-1, grid))
    row_idx, grid = answers[0]
    row = grid[row_idx]

    row_idx, grid = answers[1]
    guess = set(row) & set(grid[row_idx])

    if len(guess) == 0:
        print "Case #%d: Volunteer cheated!" % (case + 1)
    elif len(guess) > 1:
        print "Case #%d: Bad magician!" % (case + 1)
    else:
        print "Case #%d: %d" % (case + 1, guess.pop())

