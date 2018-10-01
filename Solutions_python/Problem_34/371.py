#!/usr/bin/env python

import sys

DEBUG = 0

# A parsed line is represented as a list of strings.
def parseLine(l):
    ret = []
    seenLP = False
    for x in l:
        if x == '(':
            seenLP = True
            inParen = ''
        elif x == ')':
            assert(seenLP)
            seenLP = False
            ret.append(inParen)
        else:
            if seenLP:
                inParen = inParen + x
            else:
                ret.append(x)
    return ret

def wordsWithPrefix(prefix, words):
    ret = set()
    for w in words:
        if w[0] == prefix:
            ret.add(w[1:])
    return ret

def compute(words, wordLen, line, indent = 0):
    if DEBUG > 1:
        print '    '*indent, 'comp: w:', list(words), 'line:', line

    if len(line) != wordLen:
        ret = 0
    elif len(words) == 0:
        ret = 0
    elif line == []:
        if '' in words:
            ret = 1
        else:
            ret = 0
    else:
        ret = 0
        for c in line[0]:
            if DEBUG > 1:
                print '    '*indent, 'c:', c
            ret = ret + compute(wordsWithPrefix(c, words), wordLen-1, line[1:], indent+1)
    if DEBUG > 1:
        print '    '*indent, 'ret:', ret
    return ret

l = sys.stdin.readline().strip()
inp = l.split(' ')
L = int(inp[0])
D = int(inp[1])
N = int(inp[2])


words = set()
for i in range(0, D):
    words.add(sys.stdin.readline().strip())

print 'words:', words, 'num words:', len(words)
num = 1
for l in sys.stdin:
    l = l.strip()
    line = parseLine(l)
    if DEBUG:
        print 'l:', l, 'parsed:', line
    print 'Case #%d: %d' % (num, compute(words, L, line))
    num = num + 1
