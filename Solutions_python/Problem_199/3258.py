import os
import time

__author__ = 'ricky'


def calculate(str, k, num):
    strlen = len(str)
    i = 0
    while i < strlen:
        if str[i] == '-':
            if i + k > strlen:
                num = -1
                break

            flipstr = flip(list(str), i, k)
            num += 1
            i = strlen
            num = calculate(flipstr,k, num)
        i += 1

    return num


def flip(str, start, k):
    for i in range(start, start + k):
        if str[i] == '+':
            str[i] = '-'
        else:
            str[i] = '+'
    return "".join(str)


def read_file(input):
    i = 0
    lines = (line.rstrip('\n') for line in open(input))
    lineout = ''
    for xx in lines:
        i += 1
        if i == 1:
            continue
        arr = xx.split()
        print(arr)
        res = calculate(arr[0], int(arr[1]), 0)
        if res < 0:
            lineout = "IMPOSSIBLE"
        else:
            lineout = res
        yield ('Case #{}: {}'.format(i - 1, lineout))


if __name__ == '__main__':

    start = time.clock()
    with open('sample-data/A-small-attempt0.out', 'w') as the_file:
        for line in (read_file('sample-data/A-small-attempt0.in')):
            the_file.write(line + os.linesep)
    end = time.clock()
    print("%.2gs" % (end - start))
