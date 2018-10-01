#! /usr/bin/python3.2
# -*- coding: UTF-8 -*-

from sys import argv
from functools import reduce

class Game:

    def __init__(self, lines):
       self.squares = lines

    def normalize(c):
        if c == 'X': return 2
        if c == 'O': return 4
        if c == 'T': return 6
        if c == '.': return 0

    def sum(line):
        return reduce(lambda x,y: x&y, \
                [Game.normalize(c) for c in line], Game.normalize('T'))

    def has_empty_space(self):
        for l in self.squares:
            for c in l:
                if c == '.':
                    return True

        return False

    def lines(self):
        # lines
        for l in self.squares:
            yield list(l)

        # cols
        for i in range(0, 4):
            yield [ l[i] for l in self.squares ]

        # NE->SW
        yield [ self.squares[i][i] for i in range(0, 4) ]
        # NW->SE
        yield [ self.squares[i][3-i] for i in range(0, 4) ]


    def result(self):
        for l in self.lines():
            s = Game.sum(l)
            if (s == 2):
                return 'X won'
            if (s == 4):
                return 'O won'

        if self.has_empty_space():
            return 'Game has not completed'

        return 'Draw'

if __name__ == '__main__':

    f = open(argv[1], 'r')
    count, *lines = f.readlines();
    f.close()

    lines = [ l.replace('\n', '') for l in lines if not l == '\n']

    f = open('tictac.output', 'w')
    for i in range(0, int(count)):
        f.write("Case #" + str(i+1) + ": ")
        g = Game(lines[i*4:(i+1)*4])
        f.write(g.result() + '\n')

    f.close()
