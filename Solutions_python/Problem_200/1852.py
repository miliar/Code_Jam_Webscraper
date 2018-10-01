#!/bin/python3


def tidySeq(seq):
    for i in range(len(seq) - 1):
        if int(seq[i]) > int(seq[i + 1]):
            return i
    return -1

T = int(input().strip())
for test in range(T):
    seq = list(input().strip())
    index = tidySeq(seq)
    while index != -1:
        seq = seq[:index] + [str(int(seq[index]) - 1)] + \
            ['9'] * len(seq[index + 1:])
        index = tidySeq(seq)
    print('Case #%d: %d' % ((test + 1), (int(''.join(seq)))))
