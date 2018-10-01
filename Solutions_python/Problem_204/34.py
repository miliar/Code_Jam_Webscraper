# Python 3.5.2

from common import *

def main(casenum):
    n, p = readints()
    rs = readints()
    qss = []
    for i in range(n):
        qss.append(readints())
    for i in range(n):
        qss[i].sort()

    for i in range(n):
        for j in range(p):
            q = qss[i][j] * 100
            low = 1 + (q - 1) // (rs[i] * 110)
            high = q // (rs[i] * 90)
            low = max(1, low)
            qss[i][j] = (low, high)

    count = 0
    while True:
        if len(qss[0]) == 0:
            break
        least = qss[0][-1][1]
        done = False
        for i in range(n):
            if len(qss[i]) == 0:
                done = True
                break
            least = min(least, qss[i][-1][1])
        if done:
            break

        okay = True
        for i in range(n):
            if qss[i][-1][0] > least:
                okay = False
                qss[i].pop()

        if okay:
            count += 1
            for i in range(n):
                qss[i].pop()

    writecase(casenum, count)

run(main)
