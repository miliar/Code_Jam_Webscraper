#!/usr/bin/python

import re
import string
import sys

def check(board, K):
    cb = []
    X = len(board)
    red = False
    blue = False
    for row in board:
        s = ""
        for c in row:
            if c != '.':
                s += c
        cb.append(string.rjust(s, X, "."))
    for row in range(X):
        rc = 0
        bc = 0
        for col in range(X):
            if cb[row][col] == "B":
                (rc, bc) = (0, bc + 1)
                if bc >= K:
                    blue = True
                    if red: return "Both"
            elif cb[row][col] == "R":
                (rc, bc) = (rc + 1, 0)
                if rc >= K:
                    red = True
                    if blue: return "Both"
            else:
                (rc, bc) = (0, 0)
    for col in range(X):
        rc = 0
        bc = 0
        for row in range(X):
            if cb[row][col] == "B":
                (rc, bc) = (0, bc + 1)
                if bc >= K: 
                    blue = True
                    if red: return "Both"
            elif cb[row][col] == "R":
                (rc, bc) = (rc + 1, 0)
                if rc >= K:
                    red = True
                    if blue: return "Both"
            else:
                (rc, bc) = (0, 0)
    for diag in range(2 * X):
        (rc, bc) = (0, 0)
        for row in range(X):
            col = diag + row
            if col < X and col >= 0 and row < X and row >= 0:
                if cb[row][col] == "B":
                    (rc, bc) = (0, bc + 1)
                    if bc >= K: 
                        blue = True
                        if red: return "Both"
                elif cb[row][col] == "R":
                    (rc, bc) = (rc + 1, 0)
                    if rc >= K:
                        red = True
                        if blue: return "Both"
                else:
                    (rc, bc) = (0, 0)
    for diag in range(2 * X):
        (rc, bc) = (0, 0)
        for row in range(X):
            col = diag - row
            if col < X and col >= 0 and row < X and row >= 0:
                if cb[row][col] == "B":
                    (rc, bc) = (0, bc + 1)
                    if bc >= K: 
                        blue = True
                        if red: return "Both"
                elif cb[row][col] == "R":
                    (rc, bc) = (rc + 1, 0)
                    if rc >= K:
                        red = True
                        if blue: return "Both"
                else:
                    (rc, bc) = (0, 0)
    if red and blue:
        return "Both"
    if red:
        return "Red"
    if blue:
        return "Blue"
    return "Neither"

f = open(sys.argv[1])

num_cases = int(f.readline())

for n in range(1, num_cases + 1):
    arr = f.readline().split()
    X = int(arr[0])
    K = int(arr[1])
    board = []
    for i in range(X):
        board.append(f.readline()[:X])
    print "Case #%d: %s" % (n, check(board, K))

