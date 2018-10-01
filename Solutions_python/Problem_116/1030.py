import sys


def determine_gamestate(board):
    winX = test_won(board, "X")
    winO = test_won(board, "O")
    if winX and not winO:
        return "X won"
    elif winO and not winX:
        return "O won"
    elif test_finished(board):
        return "Draw"
    else:
        return "Game has not completed"


def test_finished(board):
    return not any((item == '.') for row in board for item in row)


def test_won(board, sign):
    return any(test_combination(comb, sign) for comb in get_possible_combinations(board))


def test_combination(combination, sign):
    return all(x in [sign, "T"] for x in combination)


def get_possible_combinations(board):
    return [
        [board[0][0], board[1][0], board[2][0], board[3][0]],
        [board[0][1], board[1][1], board[2][1], board[3][1]],
        [board[0][2], board[1][2], board[2][2], board[3][2]],
        [board[0][3], board[1][3], board[2][3], board[3][3]],

        [board[0][0], board[0][1], board[0][2], board[0][3]],
        [board[1][0], board[1][1], board[1][2], board[1][3]],
        [board[2][0], board[2][1], board[2][2], board[2][3]],
        [board[3][0], board[3][1], board[3][2], board[3][3]],

        [board[0][0], board[1][1], board[2][2], board[3][3]],
        [board[0][3], board[1][2], board[2][1], board[3][0]]
    ]


def get_boards(path):
    with open(path) as f:
        lines = f.readlines()

    num_boards = int(lines[0])
    return num_boards, ([lines[5*i+j] for j in range(1, 5)] for i in range(num_boards))

if __name__ == '__main__':
    print(sys.argv[1])
    num_boards, boards = get_boards(sys.argv[1])
    for i in range(num_boards):
        print("Case #{gamenum}: {gamestate}".format(gamenum=i+1, gamestate=determine_gamestate(boards.__next__())))

