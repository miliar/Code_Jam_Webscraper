import sys

def score(four):
    total = 1
    four = four.replace("X", "1").replace("O", "5").replace("T", "9").replace(".", "0")
    for char in four:
        total *= int(char)

    if total == 9 or total == 1:
        return "X won"
    elif total == 625 or total == 1125:
        return "O won"
    else:
        return ""

def find_board_state(board):
    #rows
    for row in board:
        outcome = score(row)
        if outcome:
            return outcome

    #columns
    outcome = score(board[0][0] + board[1][0] + board[2][0] + board[3][0])
    if outcome:
        return outcome
    outcome = score(board[0][1] + board[1][1] + board[2][1] + board[3][1])
    if outcome:
        return outcome
    outcome = score(board[0][2] + board[1][2] + board[2][2] + board[3][2])
    if outcome:
        return outcome
    outcome = score(board[0][3] + board[1][3] + board[2][3] + board[3][3])
    if outcome:
        return outcome

    #diagonals
    outcome = score(board[0][0] + board[1][1] + board[2][2] + board[3][3])
    if outcome:
        return outcome
    outcome = score(board[3][0] + board[2][1] + board[1][2] + board[0][3])
    if outcome:
        return outcome


    dot_found = False
    for row in board:
        if "." in row:
            dot_found = True
            break
    if dot_found:
        return "Game has not completed"
    else:
        return "Draw"


if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin]
    i = 1
    for j, game in enumerate(range(int(lines[0]))):
        board = lines[i:i+4]
        print "Case #%d: %s" % (j +1, find_board_state(board))
        i += 5