import numpy as np
import sys
import heapq
import copy
import re

class Board(object):

    def __init__(self, r, c):
        self.board = np.zeros((r, c), dtype=int)
        self.board.fill(-1)
        self.used = set()
        self.r = r
        self.c = c

    def is_winning(self):
        ret = False
        n = self.board[self.board >= 0].size

        for x in range(self.r):
            for y in range(self.c):
                if (x, y) not in self.used:
                    continue

                v = self.board[x][y]
                if v == -1:
                    continue
                if v == 0:
                    ret = True
                elif v > 0:
                    if not self.has_around(x, y, 0) and n > 1:
                        return False

        if n == 1:
            ret = True

        return ret

    def mark_used(self, x, y):
        self.used.add((x, y))

        self.board[x][y] = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                try:
                    nx = x + dx
                    ny = y + dy

                    if (nx, ny) in self.used and nx >= 0 and nx < self.r and ny >= 0 and ny < self.c:
                        self.board[nx][ny] = self.mines_around(nx, ny)
                except:
                    pass

    def sum(self):
        s = self.board[self.board > 0].sum()
        return s + (self.r * self.c) - self.board[self.board == 0].size

    def mines(self):
        return self.board[self.board == -1].size

    def mines_around(self, x, y):
        return self.has_around(x, y, -1)

    def has_around(self, x, y, v):
        s = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                try:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < self.r and ny >= 0 and ny < self.c:

                        if self.board[nx][ny] == v:
                            s += 1
                except:
                    pass
        return s

    def is_used(self, x, y):
        return (x, y) in self.used

    def copy(self):
        return copy.deepcopy(self)

    def try_open(self):
        for x, y in self.used:
            lst = [(x, y)]
            steped = set()
            while lst:
                x, y = lst.pop()
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx = dx + x
                        ny = dy + y
                        if (nx, ny) in self.used and (nx, ny) not in steped:
                            if self.board[x][y] == 0 or len(self.used) == 1:
                                lst.append((nx, ny))
                                steped.add((nx, ny))
                            #elif self.board[x][y] > 0 and self.board[nx][ny] == 0:
                            #    lst.append((nx, ny))
                            #    steped.add((nx, ny))

            if steped == self.used:
                return (x, y)


if __name__ == '__main__':

    test_cases = int(sys.stdin.readline().strip())

    for i in range(test_cases):
        r, c, m = map(int, sys.stdin.readline().strip().split())

        board = Board(r, c)
        if r * c > m:
            board.mark_used(0, 0)

        heap = []
        heapq.heappush(heap, (board.sum(), (0, 0, board)))

        won = None
        while heap:
            s, (x, y, board) = heapq.heappop(heap)

            if board.mines() > m:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx = x + dx
                        ny = y + dy

                        if nx >= r or ny >= c or nx < 0 or ny < 0:
                            continue

                        if board.is_used(nx, ny):
                            continue

                        nb = board.copy()
                        nb.mark_used(nx, ny)
                        heapq.heappush(heap, (nb.sum(), (nx, ny, nb)))

            elif board.mines() == m:
                if board.is_winning():
                    won = board.board
                    break

        print 'Case #{}:'.format(i + 1)
        if won is None or board.try_open() is None:
            print 'Impossible'
        else:
            v = str(won).replace('-1', '*').replace('[', '').replace(']', '').replace(' ', '')
            v = re.sub('[0-9]', '.', v) 
            v = 'c' + v[1:]
            print v
