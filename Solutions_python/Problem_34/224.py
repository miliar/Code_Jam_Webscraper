#!/usr/bin/env python

import re
import sys

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()

    parts = lines[0].strip().split()
    L, D, N = map(int, parts)

    words = []
    for i in range(1, 1+D):
        words.append(lines[i].strip())

    for case in range(N):
        solution = solve(L, words, lines[case + D + 1].strip())
        print "Case #%d: %d" % (case+1, solution)

def solve(L, words, word):
    parts = []

    i = 0
    while i < len(word):
        if word[i] not in ['(', ')']:
            parts.append([word[i]])
            i += 1
        elif word[i] == '(':
            i += 1
            t = []
            while word[i] != ')':
                t.append(word[i])
                i += 1
            parts.append(t)
            i += 1

    matches = words[:]

    for i in range(L):
        matches = [m for m in matches if m[i] in parts[i]]

    return len(matches)

if __name__ == '__main__':
    main()