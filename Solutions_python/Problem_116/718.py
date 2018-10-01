def isWinner(seq):
    if '.' in seq:
        return False
    elif seq in isWinner.cache:
        return isWinner.cache[seq]
    else:
        prevCell = None
        winner = True
        for cell in seq:
            # print(cell)
            if prevCell is None:
                prevCell = cell if cell != 'T' else None
            else:
                if cell != prevCell and cell != 'T':
                    winner = False
                    break
        if winner is True:
            answer = isWinner.cache[seq] = prevCell + ' won'
        else:
            answer = isWinner.cache[seq] = False
        return answer



isWinner.cache = {
    'TTTT': False
}

def answer(game):

    for row in game:
        outcome = isWinner("".join(row))
        if outcome != False:
            return outcome

    for col in range(4):
        outcome = isWinner("".join([ game[0][col], game[1][col], game[2][col], game[3][col] ]))
        if outcome != False:
            return outcome

    diagOne = isWinner("".join([ game[0][0], game[1][1], game[2][2], game[3][3] ]))
    if diagOne != False:
        return diagOne

    diagTwo = isWinner("".join([ game[0][3], game[1][2], game[2][1], game[3][0] ]))
    if diagTwo != False:
        return diagTwo


    size = len([cell for row in game for cell in row if cell != '.'])
    return 'Draw' if size == 16 else 'Game has not completed'

def codejam_read(filen):
    f = open(filen,'r')
    fout = open(filen[:-2] + "out", 'w')
    case_num = 1
    line_num = 0
    test_size = f.readline()
    game = []
    for line in f:
        line_num += 1
        listline = list(line.rstrip())

        if line_num != 5:
            game.append(listline)
            if line_num == 4:
                # print("Case #{0}: {1}".format(case_num, answer(game)))
                fout.write("Case #{0}: {1}\n".format(case_num, answer(game)))
                case_num += 1
                # break
        elif line_num == 5:
            game = []
            line_num = 0
    fout.close()
    f.close()


codejam_read('A-large.in')
