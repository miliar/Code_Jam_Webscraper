import os

class Board(object):

    def __init__(self, rows):

        self.rows = rows
        self.cols = [''.join(r[i] for r in rows) for i in range(4)]
        self.d1 = [''.join(r[i]) for i, r in enumerate(rows)]
        self.d2 = [''.join(r[3-i]) for i, r in enumerate(rows)]
        self.all = self.rows + self.cols + [self.d1] + [self.d2]

    def outcome(self):
        """
        "X won" (the game is over, and X won)
        "O won" (the game is over, and O won)
        "Draw" (the game is over, and it ended in a draw)
        "Game has not completed" (the game is not over yet)
        """
        def _outcome(row):
            if '.' not in row and 'O' not in row:
                return 'X won'
            elif '.' not in row and 'X' not in row:
                return 'O won'
            return None
        for row in self.all:
            o = _outcome(row)
            if o:
                return o

        # if we get down here it's either a draw or an incomplete game
        for row in self.rows:
            if '.' in row:
                return 'Game has not completed'

        return 'Draw'

    def __repr__(self):
        return "\n".join(self.rows)

def solve(filename):
    with open(filename) as data:
        first = True
        case = 1
        gamedata = []
        for line in data:
            line = line.strip()
            if not line: continue
            if first:
                games = int(line)
                first = False
            else:
                assert len(line) == 4, 'expected line of size 4 but was %s (%s)' % (line, len(line))
                gamedata.append(line)
                if len(gamedata) == 4:
                    board = Board(gamedata)
                    print("Case #{case}: {out}".format(case=case, out=board.outcome()))
                    case += 1
                    gamedata = []


if __name__ == "__main__":
    filename = "A-large.in"
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    solve(fname)

