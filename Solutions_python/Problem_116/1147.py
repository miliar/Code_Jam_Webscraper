import sys
class Game(object):
    def __init__(self, lines):
        self.board = lines
    @property
    def x_has_won(self):
        return self.has_won('X')
    @property
    def o_has_won(self):
        return self.has_won('O')
    def has_won(self, who):
        winning_line = who * 4
        board = [line.replace('T', who) for line in self.board]
        return any([self.check_lines(board, winning_line),
                    self.check_columns(board, winning_line),
                    self.check_diagonal(board, winning_line)])
    def check_lines(self, board, winning_line):
        return any(winning_line == line for line in board)
    def check_columns(self, board, winning_line):
        column_board = [''.join(line) for line in zip(*board)]
        return self.check_lines(column_board, winning_line)
    def check_diagonal(self, board, winning_line):
        diagonal_board = ['%s%s%s%s' % (board[0][0], board[1][1], board[2][2],
                                        board[3][3]),
                          '%s%s%s%s' % (board[0][3], board[1][2], board[2][1],
                                        board[3][0])]
        return self.check_lines(diagonal_board, winning_line)
    @property
    def has_free_squares(self):
        return any(['.' in line for line in self.board])
    @property
    def status_line(self):
        if self.x_has_won:
            return "X won"
        if self.o_has_won:
            return "O won"
        if not self.has_free_squares:
            return "Draw"
        return "Game has not completed"

def get_game(infile):
    lines = []
    for i in range(4):
        lines.append(infile.readline()[:-1])
    infile.readline()
    return Game(lines)

filename = sys.argv[1]
with open(filename)as infile:
    with open('.'.join([filename.split('.')[0], 'out']), 'w') as outfile:
        cases = int(infile.readline())
        for case in range(cases):
            game = get_game(infile)
            solution = "Case #%d: %s\n" % (case + 1, game.status_line)
            outfile.write(solution)
