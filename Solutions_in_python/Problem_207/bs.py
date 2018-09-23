import sys
from collections import Counter
import itertools
import numpy as np


def get_line(format, line=None, extract_if_one=True):
    line = next(sys.stdin) if line is None else line
    types = {
        'i': int,
        'f': float,
        's': str,
    }
    line = line.strip().split(' ')
    assert len(line) == len(format)
    for i, t in enumerate(format):
        line[i] = types[t](line[i])
    return tuple(line) if len(line) > 1 or not extract_if_one else line[0]

class Problem:
    def get_max_color(self, last_color):
        max_cnt = 0
        max_c = None
        if last_color == 'G':
            return 'R'
        if last_color == 'V':
            return 'Y'
        if last_color == 'O':
            return 'B'
        if last_color != 'R' and self.r > max_cnt:
            max_cnt = self.r
            max_c = 'R'
        if last_color != 'B' and self.b > max_cnt:
            max_cnt = self.b
            max_c = 'B'
        if last_color != 'Y' and self.y > max_cnt:
            max_cnt = self.y
            max_c = 'Y'
        if max_c is None:
            assert False
        return max_c

    def __init__(self):
        n, r, o, y, g, b, v = get_line('iiiiiii')
        self.r, self.o, self.y, self.g, self.b, self.v = r, o, y, g, b, v
        hn = (n - g - o - v) / 2
        self.sol = None
        if r < g or b < o or y < v:
            return
        if r-g > hn or b-o > hn or y-v > hn:
            return
        self.sol = []
        last_color = 'none'
        while n > 0:
            # print(self.sol)
            n -= 1
            c = self.get_max_color(last_color)
            if c == 'R':
                self.sol.append('R')
                self.r -= 1
                if self.g > 0:
                    self.sol.append('G')
                    self.g -= 1
                    n -= 1
                    # self.sol.append('R')
                    # self.r -= 1
                    # n -= 1
            elif c == 'Y':
                self.sol.append('Y')
                self.y -= 1
                if self.v > 0:
                    self.sol.append('V')
                    self.v -= 1
                    n -= 1
                    # self.sol.append('Y')
                    # self.y -= 1
                    # n -= 1
            elif c == 'B':
                self.sol.append('B')
                self.b -= 1
                if self.o > 0:
                    self.sol.append('O')
                    self.o -= 1
                    n -= 1
                    # self.sol.append('B')
                    # self.b -= 1
                    # n -= 1
            last_color = self.sol[-1]
        if self.sol[0] == self.sol[-1]:
            t = self.sol[-1]
            self.sol[-1] = self.sol[-2]
            self.sol[-2] = t

    def solve(self):
        if self.sol is None:
            print('IMPOSSIBLE')
            return
        # if self.sol[0] == self.sol[-1]:
        #     print('IMPOSSIBLE')
        #     return
        #
        # shit = [self.sol[0], self.sol[-1]]
        # if 'R' in shit and ('O' in shit or 'V' in shit):
        #     print('IMPOSSIBLE')
        #     return
        # if 'B' in shit and ('G' in shit or 'V' in shit):
        #     print('IMPOSSIBLE')
        #     return
        # if 'Y' in shit and ('O' in shit or 'B' in shit):
        #     print('IMPOSSIBLE')
        #     return

        print(''.join(self.sol))


def main():

    # sys.stdin = open('b.in', 'r')
    sys.stdin = open('B-small-attempt2.in', 'r')
    sys.stdout = open('bs.out', 'w')
    T = get_line('i')
    for i in range(T):
        print('Case #%d: ' % (i+1, ), end='')
        p = Problem()
        p.solve()


if __name__ == '__main__':
    main()
