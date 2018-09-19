#!/usr/bin/env python
from __future__ import print_function

welcome = "welcome to code jam"
welcomeSet = set(welcome)

def init(case):
    found = 0
    pos = 0
    where = {}
    for letter in welcomeSet:
        where[letter] = [-1]

    for letter in case:
        if found == 0 and letter != welcome[0]:
            continue
        found = 1
        if letter in welcomeSet:
            if letter in where:
                where[letter] += [pos]
            else:
                where[letter] = [pos]
        pos += 1

#    print(where)
    return where

class Node:
    def __init__(self, letter, pos):
        self.letter = letter
        self.pos = pos
        self.children = []

def make_tree(msg, parent, where, count):
    if len(where) == 0:
        return 0
    if len(msg) == 0:
        return 1

    count = 0
    letter = msg[0]
    for p in where[letter]:
        if p > parent.pos:
            node = Node(letter, p)
            parent.children.append(node)
            count += make_tree(msg[1:], node, where, count)
    return count

#
# main
#
N = int(raw_input())
print(N, "cases")

out = open("out", "w")

for i in range(1, N + 1):
    case = raw_input()
    print("Case #%d:\n  %s" % (i, case))
    root = Node("ROOT", -1)
    count = make_tree(welcome, root, init(case), 0)
    result = "000" + str(count)
    print("Case #%d: %s" % (i, result[-4:]), file=out)
    print("  " + result)

out.close()
