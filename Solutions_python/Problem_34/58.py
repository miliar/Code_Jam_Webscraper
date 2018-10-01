#!/usr/bin/env python

# Been a while since I've done any Python

words = []

def group(s):
    sep = False
    ret = []

    for c in s:
        if c == '(':
            sep = True
            ret.append("")
        elif c == ')':
            sep = False
        elif sep:
            ret[-1] = "%s%c" % (ret[-1], c)
        else:
            ret.append(c)

    return ret

def matches(s):
    gset = [set(st) for st in group(s)]
    ret = 0
    for word in words:
        flag = True
        for i, c in enumerate(word):
            if not c in gset[i]:
                flag = False
                break
        if flag:
            ret += 1
    return ret

if __name__ == "__main__":
    l, d, n = map(int, raw_input().split(' '))
    words = [raw_input() for i in xrange(d)]
    
    for i in xrange(n):
        print "Case #%d: %d" % (i + 1, matches(raw_input()))


