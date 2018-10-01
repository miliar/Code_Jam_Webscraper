from __future__ import division, print_function

import sys
import logging
from collections import Counter
from pprint import pformat

log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


3

5

9
"""
....x....
.x..x....
.x..x.x..
.xx.x.x..
.xx.x.xx.




16
.......x........ 1 8/7
.......x...x.... 2 4/3
...x...x...x.... 3 3/3
...x...x...x.x.. 4 2/1
.x.x...x...x.x.. 5 1/1
.x.x.x.x...x.x..
.x.x.x.x.x.x.x..
.x.x.x.x.x.x.xx. 8 1/0
xx.x.x.x.x.x.xx. 9 0/0


15
.......x....... 1 7/7
...x...x....... 2 3/3
...x...x...x...
.x.x...x...x... 4 1/1
.x.x...x.x.x...
.x.x.x.x.x.x...
.x.x.x.x.x.x.x.
xx.x.x.x.x.x.x. 8 0/0

11

.....x..... 1 5/5
..x..x..... 2 2/2
..x..x..x..
x.x..x..x.. 4 1/0
x.xx.x..x..
x.xx.xx.x..
x.xx.xx.xx.
xxxx.xx.xx. 8 0/0


23
...........x........... 1 11/11
.....x.....x........... 2 5/5



"""

def get_input():
    with open(sys.argv[1], 'r') as f:
        return f.readlines()[1:]



def solve_exp(n, k):
    x = 1
    div = 2 ** x
    g = 0
    log.debug('SOLVE: {} {}'.format(n, k))
    while div <= n:
        v = n // div
        if k > v:
            return g, g
        elif k == v:
            if n % 2 == 0:
                # even starting n
                return g + 1, g
            else:
                return g, g
        log.debug('PASS: {} | {} | {} | {} | {}'.format(k, v, g, x, div))
        g += 2 ** (x-1)
        x += 1
        div = 2 ** x
    raise ValueError('What?')



CACHE = {}

def solve(n, k):
    c = Counter([n])
    for i in range(k):
        v = max(c.keys())
        c[v] -= 1
        if c[v] == 0:
            del c[v]
        gmin = v // 2
        gmax = v - gmin - 1
        c[gmin] += 1
        c[gmax] += 1
    return gmin, gmax


def main():
    lines = get_input()
    for i, line in enumerate(lines):
        n, k = map(int, line.split())
        gmin, gmax = solve(n, k)
        print('Case #{}: {} {}'.format(i + 1, gmin, gmax))


if __name__ == '__main__':
    main()
