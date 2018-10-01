#!/usr/bin/env python3
import copy
import itertools
import sys

class Board():
    def __init__(self, r, c):
        self._board = [['*' for col in range(c)] for row in range(r)]
        self._r = r
        self._c = c
        self._p = 0

    def disp(self):
        for row in self._board:
            print(''.join(row))

    def place(self, s):
        assert self._board[s[0]][s[1]] == '*'
        self._board[s[0]][s[1]] = '.'
        self._p += 1

    def unplace(self, s):
        assert self._board[s[0]][s[1]] == '*'
        self._board[s[0]][s[1]] = '.'

    def adj(self, s):
        x, y = s
        if x > 0:
            yield (x-1, y)
        if y > 0:
            yield (x, y-1)
        if x > 0 and y > 0:
            yield (x-1, y-1)
        if x+1 < self._r:
            yield (x+1, y)
        if y+1 < self._c:
            yield (x, y+1)
        if x+1 < self._r and y+1 < self._c:
            yield (x+1, y+1)
        if x+1 < self._r and y > 0:
            yield (x+1, y-1)
        if x > 0 and y+1 < self._c:
            yield (x-1, y+1)

    def test(self, s):
        if self._board[s[0]][s[1]] != '.':
            return False
        board = copy.deepcopy(self._board)
        p = self._p
        def expand(s):
            nonlocal p
            if board[s[0]][s[1]] == ',':
                return
            assert board[s[0]][s[1]] == '.'
            clean = True
            for x, y in self.adj(s):
                if board[x][y] == '*':
                    clean = False
            board[s[0]][s[1]] = ','
            p -= 1
            if clean:
                for q in self.adj(s):
                    expand(q)
        expand(s)
        return not p

    def testAll(self):
        for i in range(0, self._r):
            for j in range(0, self._c):
                if self.test((i, j)):
                    return (i, j)
        return False

    def click(self, s):
        self._board[s[0]][s[1]] = 'c'
        self.disp()


if len(sys.argv) > 1 and sys.argv[1] == 'lookup':
    with open(sys.argv[2]) as f:
        l = f.read().splitlines()
    i = 0
    d = {}
    while i < len(l):
        s = tuple(int(x) for x in l[i].split(' '))
        if l[i+1] == 'Impossible':
            d[s] = 'Impossible'
            i += 2
        else:
            j = i+1+s[0]
            d[s] = '\n'.join(l[i+1:j])
            i = j

    cases = int(input())
    for case in range(1, cases+1):
        s = tuple(int(x) for x in input().split(' '))
        print("Case #%d:\n%s" % (case, d[s]))
else:
    cases = int(input())
    for case in range(1, cases+1):
        r, c, m = [int(x) for x in input().split(' ')]
        if len(sys.argv) > 1:
            print(r, c, m)
        else:
            print("Case %d:" % case)
        g = r*c - m

        win = False
        for s in itertools.combinations(
                ((x, y) for x in range(0, r) for y in range(0, c)), g):
            b = Board(r, c)
            for p in s:
                b.place(p)
            p = b.testAll()
            if p:
                b.click(p)
                win = True
                break
        if not win:
            print("Impossible")
