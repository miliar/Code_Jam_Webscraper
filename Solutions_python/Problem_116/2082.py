# coding: utf8

import sys


OUTPUT_TEMPLATE = 'Case #{0}: {1}\n'
WON_TEMPLATE = '{0} won'


class Board(object):
    def __init__(self, board):
        self.has_empty_field = False
        self.horizontal = []
        self.vertical = []
        self.diagonal = []

        for line in board:
            if '.' in line and not self.has_empty_field:
                self.has_empty_field = True

            self.horizontal.append([i for i in line])

        self.vertical = zip(*self.horizontal)

        self.diagonal.append([l[n] for n, l in enumerate(self.horizontal)])
        self.diagonal.append([l[len(self.horizontal) - 1 - n] for n, l in enumerate(self.horizontal)])

    @staticmethod
    def checkEqualOrT(list_):
        if '.' in list_:
            return False

        if 'T' in list_:
            return len(set(list_)) == 2

        return len(set(list_)) == 1

    def determineWinner(self):
        for route in [self.horizontal, self.vertical, self.diagonal]:
            for piece in route:
                if isinstance(piece, tuple):
                    piece = list(piece)

                if self.checkEqualOrT(piece) is True:
                    if 'T' in piece:
                        piece.pop(piece.index('T'))

                    return WON_TEMPLATE.format(piece[0])

        if not self.has_empty_field:
            return 'Draw'

        return 'Game has not completed'


if __name__ == '__main__':
    fp = open(sys.argv[1], 'rb')

    num_of_maps = int(fp.readline())

    for i in xrange(num_of_maps):
        current_map = []

        for line in fp:
            if line == '\n':
                board = Board(current_map)

                output = open('output.txt', 'ab')
                output.write(OUTPUT_TEMPLATE.format(i + 1, board.determineWinner()))
                output.close()

                break

            current_map.append(line[:4])

    fp.close()
