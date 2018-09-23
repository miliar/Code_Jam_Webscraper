import io
import re
import sys
from heapq import *
from itertools import *


def solve(rows):
    empty_rows = [bool(re.match(r'\?+$', row)) for row in rows]
    if empty_rows[0]:
        n = len(list(takewhile(lambda x: x, empty_rows)))
        return solve([rows[n]] * (n + 1) + rows[n + 1:])
    for i, is_empty in enumerate(empty_rows):
        if is_empty:
            rows[i] = rows[i - 1]
    return [''.join(solve(re.findall(r'.', row))) for row in rows] if len(rows[0]) > 1 else rows

# solve(['???', 'xxx'])
# solve(['???', '???', 'xxx'])
# solve(['xxx', '???', 'yyy'])
# solve(['xxx', '???', '???'])

# solve(["G??", "?C?", "??J"])

# solve(["CODE", "????", "?JAM"])
# solve(["CA", "KE"])

T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    print('Case #%d:' % (t + 1))
    board = [input() for _ in range(R)]
    board = solve(board)
    print('\n'.join(board))
