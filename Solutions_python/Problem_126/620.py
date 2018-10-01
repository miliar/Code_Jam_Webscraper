# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser
# import string

# Input
#
# 4
# quartz 3
# straight 3
# gcj 2
# tsetse 2
#
# Output
#
# Case #1: 4
# Case #2: 11
# Case #3: 3
# Case #4: 11


def process_sub(sub, l, r):
    # print sub
    count = 0
    for i in xrange(l + r + 1):
        # print 'i', i, 'l', l, 'r', r, l + r + 1
        count += i + 1
        # print 'count_init', count
        if l < i:
            count += l - i
            # print 'lcount', count
        if r < i:
            count += r - i
            # print 'rcount', count
        # print l, r, count
    return count


def process_block(name, name_len, block, n, pos):
    count = 0
    # print block
    for i in xrange(len(block) - n + 1):
        sub = block[i:i + n]
        # print 'sub', sub
        # print 'name', name
        lind = name.find(sub, pos + 1)
        rind = lind + n
        l = lind - pos - 1
        # print 'lind', lind, 'pos', pos
        r = name_len - rind
        count += process_sub(sub, l, r)
        pos = lind
    return count, pos


def solve(*lines):
    name, n = lines
    name_len = len(name)
    vowels = frozenset('aeiou')
    # print 'vowels', vowels
    count = 0
    n = int(n)
    blocks = name
    for c in name:
        if c in vowels:
            blocks = blocks.replace(c, ' ')
    blocks = blocks.split()
    # print 'blocks', blocks
    pos = -1
    for block in blocks:
        if len(block) < n:
            continue
        block_count, pos = process_block(name, name_len, block, n, pos)
        count += block_count
    return count


@iter_parser
def parse(nxtline):
    return nxtline().split()


if __name__ == "__main__":
    from codejam import CodeJam
    # import ipdb; ipdb.set_trace()
    CodeJam(parse, solve).main()
