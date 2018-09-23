#!/usr/bin/python3
# A_oversized_pancake_flipper.py
# Last Updated: 2017.04.08
# Jun Go gojun077@gmail.com
#
# GCJ 2017 Qualification Round
# Problem A. Oversized Pancake Flipper
# https://code.google.com/codejam/contest/3264486/dashboard#s=p0


def flipit(L):
    """
    ListOfInts -> ListOfInts

    Given a list of ints composed of +1 and -1, return a
    list of reverse sign

    >>> flipit([-1, 1, -1])
    [1, -1, 1]

    >>> flipit([1, 1, 1])
    [-1, -1, -1]
    """
    flippedL = [i * -1 for i in L]
    return flippedL


def parseBoard(strS):
    """
    String -> List (list of ints and int)

    Given a string representing an array of pancakes and an integer,
    return a List containing a list of integers and an integer
    'K' representing the length of the pancake flipper

    >>> parseBoard('---+-++- 3')
    [[-1, -1, -1, 1, -1, 1, 1, -1], 3]

    >>> parseBoard('+++++ 4')
    [[1, 1, 1, 1, 1], 4]

    >>> parseBoard('-+-+- 4')
    [[-1, 1, -1, 1, -1], 4]
    """
    boardL = strS.split()
    pancakeS = boardL[0]
    pancakeL = []

    for char in pancakeS:
        if char == '+':
            pancakeL.append(1)
        elif char == '-':
            pancakeL.append(-1)

    K = int(boardL[1])

    return [pancakeL, K]


def allHappy(L):
    """
    List -> Boolean

    Given an integer list of pancake face-up/face-down status
    (1, -1), return True is all pancakes are face up; otw return
    False

    >>> allHappy([1, 0, 1])
    False

    >>> allHappy([1, 1, 1])
    True
    """
    happyFlag = True

    for i in L:
        if i != 1:
            happyFlag = False
            return happyFlag
    return happyFlag


def howManyFlips(strS):
    """
    String -> int

    Given a string of the form '---+-++- 3' containing the face-up
    face-down configuration of a row of pancakes, and the length
    of the pancake flipper,

    Return the number of flips required until all pancakes are
    face up (denoted by a list of all ones [1, 1, 1, ..., 1]

    ALGORITHM: If the current list element is -1, flip K elements
    starting from the current index to the opposite sign. The base
    cases are when all pancakes are already face-up and when it
    is impossible to make all pancakes face-up for the given value
    of K and the pancake configuration.

    >>> howManyFlips('---+-++- 3')
    3

    >>> howManyFlips('+++++ 4')
    0

    >>> howManyFlips('-+-+- 4')
    'IMPOSSIBLE'

    >>> howManyFlips('+--- 3')
    1
    """
    parseMe = parseBoard(strS)
    board, K = parseMe[0], parseMe[1]

    flip_cnt = 0
    board_sum = sum(board)

    # if all pancakes are already face up...
    if board_sum == len(board):
        return flip_cnt
    else:
        for h in range(0, len(board)):
            if board[h] == -1:
                if h+K <= len(board):
                    board[h:h+K] = flipit(board[h:h+K])
                    flip_cnt += 1
#        print("Changed board: %s" % board)
        if board.count(-1) < K:
            if board.count(-1) > 0:
                return 'IMPOSSIBLE'
        return flip_cnt


# MAIN PROGRAM
if __name__ == '__main__':
    import doctest
    doctest.testmod()


num_cases = int(input())
casesL = []

for i in range(num_cases):
    casesL.append(input())

case_num = 1
for j in casesL:
    ans = str(howManyFlips(j))
    print("Case #%d: %s" % (case_num, ans))
    case_num += 1
