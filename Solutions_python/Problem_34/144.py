import re
import sys

def f(exp):
    r = ""
    dep = 0
    for c in exp:
        if c == ')':
            dep = 0
        if dep == 1 and lastc != '(':
            r += '|'
        if c == '(':
            dep = 1
        r += c
        lastc = c
    return r


l,d,n = raw_input().split(' ')

l = int(l)
d = int(d)
n = int(n)
words = []

for i in range(d):
    words.append(raw_input())

for i in range(n):
    print "Case #%d:" % (i+1),
    r = raw_input()
    r = f(r)
    exp = re.compile("^" + r + "$")
    q = 0
    for j in words:
        if exp.search(j):
            q+=1
    print q
