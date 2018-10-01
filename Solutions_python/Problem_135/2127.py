__author__ = 'Servy'

import sys


def read_row():
    row = int(sys.stdin.readline().strip());
    for i in range(1, 5):
        if i == row:
            result = set(map(int, sys.stdin.readline().split()))
        else:
            sys.stdin.readline()
    return result


testNumber = int(sys.stdin.readline().strip())
for test in range(1, testNumber + 1):
    firstAttempt = read_row()
    secondAttempt = read_row()
    answers = firstAttempt.intersection(secondAttempt)
    if len(answers) == 0:
        print("Case #%d: Volunteer cheated!" % test)
    elif len(answers) == 1:
        print("Case #%d: %d" % (test, list(answers)[0]))
    else:
        print("Case #%d: Bad magician!" % test)