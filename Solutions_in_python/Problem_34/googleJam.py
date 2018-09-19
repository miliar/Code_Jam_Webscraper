#coding=utf-8
import re


def getPossibleStrings(s, l):
    poss = []
    items = []
    
    for i in range(l):
        items.append([])
    
    left = False
    right = False
    
    i = 0
    for c in s:
        if c == '(':
            left = True
            continue
        if c == ')':
            left = False
            i += 1
            continue
        
        if left:
            items[i].append(c)
        else:
            items[i].append(c)
            i += 1
            
    return items

def CheckWord(items, word):
    i = 0
    for w in word:
        if w not in items[i]:
            return False
        i += 1
    return True

if "__main__" == __name__:
    f = open("in.txt", 'r')
    l, d, n = f.readline().split(' ')
    l = int(l)
    d = int(d)
    n = int(n)
    print l, d, n
    
    print "words:"
    words = []
    for i in range(d):
        words.append(f.readline().strip())
    print words
    
    print "Tests:"
    tests = []
    for i in range(n):
        tests.append(f.readline().strip())
    print tests
    
    # do it.
    
    i = 1
    for t in tests:
        info = "Case #" + str(i) + ":"
        count = 0
        poss = getPossibleStrings(t, l)
        for word in words:
            if CheckWord(poss, word):
                count += 1
        print info, count
        i += 1