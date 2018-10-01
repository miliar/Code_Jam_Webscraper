# Python 3.2

from common import *

def main(casenum):
    n = readint()
    a = readints()

    b = list(zip(a, range(n)))
    b.sort()

    c = [x[1] for x in b]

    used = [False] * n

    count = 0
    num_done = 0

    while len(c) > 0:
        i = c.pop()

        num_left = 0
        for j in range(i):
            if used[j]:
                num_left += 1
        num_right = num_done - num_left

        count += min(num_left, num_right)

        num_done += 1
        used[i] = True

    writeline('Case #{}: {}'.format(casenum, count))

run(main)
