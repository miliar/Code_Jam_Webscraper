# tomek.py
import traceback

class Board(object):

    def __init__(self, lines, size=4):
        if len(lines) != 4:
            raise Exception('Wrong number of board lines')

        self.grid = []
        for line in lines:
            self.grid.append(line)

        self.size = size

    def __repr__(self):
        status = self.check_status()
        if status == 'X':
            return 'X won'
        elif status == 'O':
            return 'O won'
        elif status == '.':
            return 'Draw'
        else:
            return 'Game has not completed'

    def check_status(self):
        for i in range(self.size):
            if self.check_column(i) != '.':
                return self.check_column(i)
            elif self.check_row(i) != '.':
                return self.check_row(i)
            elif i < 2 and self.check_diagonal(i) != '.':
                return self.check_diagonal(i)

        if self.grid_full():
            return '.'
        
        # else return None

    def check_row(self, row):
        counts = {'X':0, 'O':0, 'T':0, '.':0}
        for column in range(self.size):
            symbol = self.grid[row][column]
            counts[symbol] += 1

        return Board.check_counts(counts)

    def check_column(self, column):
        counts = {'X':0, 'O':0, 'T':0, '.':0}
        for row in range(self.size):
            symbol = self.grid[row][column]
            counts[symbol] += 1

        return Board.check_counts(counts)

    def check_diagonal(self, index):
        if index == 0:
            slope = 1
            row = 0
        else:
            slope = -1
            row = self.size - 1

        counts = {'X':0, 'O':0, 'T':0, '.':0}
        for column in range(self.size):
            symbol = self.grid[row][column]
            counts[symbol] += 1
            row += slope

        return Board.check_counts(counts)

    def grid_full(self):
        for row in self.grid:
            for square in row:
                if square == '.':
                    return False

        return True

    @staticmethod
    def check_counts(counts):
        if counts['.'] > 0:
            return '.'
        elif counts['X'] == 4 or counts['X'] == 3 and counts['T'] > 0:
            return 'X'
        elif counts['O'] == 4 or counts['O'] == 3 and counts['T'] > 0:
            return 'O'
        else:
            return '.'

def read_file(filename):
    f = open(filename, 'r')
    results = []
    cases = int(f.readline())

    for case in range(1, cases + 1):
        lines = []
        for __ in range(4):
            lines.append(f.readline())

        result = 'Case #{0}: {1}'.format(case, Board(lines))
        results.append(result)
        print(result)

        # empty line
        f.readline()

    return results

def write_file(filename, results):
    f = open(filename, 'w')

    for line in results:
        f.write(line + '\n')

if __name__ == '__main__':
    filename = raw_input('Input Filename: ')
    results = read_file(filename)

    filename = raw_input('Output Filename: ')
    write_file(filename, results)
