

filename = 'A-large.in'
datasets = []
with open(filename, 'rt') as f:
    lines = [line.rstrip() for line in f]
    lines = [line for line in lines if line]
    testCases = int(lines[0])
    for i in range(1, len(lines), 4):
        dataset = []
        dataset.append(lines[i])
        dataset.append(lines[i + 1])
        dataset.append(lines[i + 2])
        dataset.append(lines[i + 3])
        datasets.append(dataset)


def jamout(filename, outputs):
    fout = open(filename, 'wt')
    for i, output in enumerate(outputs):
        fout.write('Case #' + str(i + 1) + ': ' + output + "\n")
    fout.close()

def determineGameStatus(board):
    
    # row checks
    winningRowsForX = ['XXXX', 'TXXX', 'XTXX', 'XXTX', 'XXXT']
    winningRowsForO = ['OOOO', 'TOOO', 'OTOO', 'OOTO', 'OOOT']
    for row in board:
        if row in winningRowsForX:
            return 'X won'
        if row in winningRowsForO:
            return 'O won'

    # column checks
    # tilt board
    tilted = [''.join([ row[x:x+1] for row in board]) for x in range(0, 4)]
    for row in tilted:
        if row in winningRowsForX:
            return 'X won'
        if row in winningRowsForO:
            return 'O won'

    # diagonal checks
    diagonals = [''.join([board[0][0], board[1][1], board[2][2], board[3][3]]),
                 ''.join([board[0][3], board[1][2], board[2][1], board[3][0]])]
    for row in diagonals:
        if row in winningRowsForX:
            return 'X won'
        if row in winningRowsForO:
            return 'O won'
        
    # not over check
    for row in board:
        if '.' in row:
            return 'Game has not completed'

    return 'Draw'


outputs = []
for dataset in datasets:
    outputs.append(determineGameStatus(dataset))

jamout('A-large.txt', outputs)
        



