# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser


def solve(*lines):
    # print lines
    round_1, round_2 = lines
    i, cards = round_1
    row_1 = cards[i]
    i, cards = round_2
    row_2 = cards[i]
    common = row_1 & row_2
    if len(common) == 0:
        return 'Volunteer cheated!'
    elif len(common) > 1:
        return 'Bad magician!'
    return list(common)[0]


@iter_parser
def parse(nxtline):
    n = 4
    for round in xrange(2):
        row = int(nxtline()) - 1
        yield row, [set(map(int, nxtline().split())) for _ in xrange(n)]


if __name__ == "__main__":
    from codejam import CodeJam
    CodeJam(parse, solve).main()
