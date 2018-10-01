#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for i in range(N)]

# Googlerese : English
dic = dict(a="y", b="h", c="e", d="s", e="o", f="c", g="v", h="x", i="d", j="u", k="i", l="g", m="l", n="b", o="k", p="r", q="z", r="t", s="n", t="w", u="j", v="p", w="f", x="m", y="a", z="q")

def a(c):
    if dic.has_key(c):
        return dic[c]
    else:
        return c

x = 0
for s in S:
    x += 1
    answer = "".join([ a(c) for c in s])
    print ("Case #%d: " + answer) % (x)

