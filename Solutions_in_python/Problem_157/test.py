#!/bin/python
import sys

def readFile(fname):
    with open(fname) as f:
            contents = f.read().splitlines()
    ncases = int(contents.pop(0))
    nlines = len(contents)/ncases
    cases = [[] for x in range(ncases)]
    c = 0
    l = 0
    for line in contents:
        cases[c].append(line)
        l += 1
        if l == nlines:
            c += 1
            l = 0
    return cases

def multiply (a, b):
    if a == '1':
        if b == '1': return (1, '1')
        if b == 'i': return (1, 'i')
        if b == 'j': return (1, 'j')
        if b == 'k': return (1, 'k')
    if a == 'i':
        if b == '1': return (1, 'i')
        if b == 'i': return (-1, '1')
        if b == 'j': return (1, 'k')
        if b == 'k': return (-1, 'j')
    if a == 'j':
        if b == '1': return (1, 'j')
        if b == 'i': return (-1, 'k')
        if b == 'j': return (-1, '1')
        if b == 'k': return (1, 'i')
    if a == 'k':
        if b == '1': return (1, 'k')
        if b == 'i': return (1, 'j')
        if b == 'j': return (-1, 'i')
        if b == 'k': return (-1, '1')

def divide (a, b):
    if a == '1':
        if b == '1': return (1, '1')
        if b == 'i': return (1, 'i')
        if b == 'j': return (1, 'j')
        if b == 'k': return (1, 'k')
    if a == 'i':
        if b == '1': return (-1, 'i')
        if b == 'i': return (1, '1')
        if b == 'j': return (-1, 'k')
        if b == 'k': return (1, 'j')
    if a == 'j':
        if b == '1': return (-1, 'j')
        if b == 'i': return (1, 'k')
        if b == 'j': return (1, '1')
        if b == 'k': return (-1, 'i')
    if a == 'k':
        if b == '1': return (-1, 'k')
        if b == 'i': return (-1, 'j')
        if b == 'j': return (1, 'i')
        if b == 'k': return (1, '1')


def reduce(a):
    res = '1'
    sign = 1
    for i in a:
        (s, res) = multiply(res, i)
        sign *= s
    return (sign, res)



def solve(case, c):
    repeat = int(case[0].split(' ')[1])
    string = case[1]*repeat
    #print(string)

    (sign, reduc) = reduce(string)
    #print("hey: (%d, %s)" % (sign, reduc))

    reduci = '1'
    signi = 1
    signRighti = sign
    reducRighti = reduc
    for i in range(0, len(string)-2):
        (s, reduci) = multiply(reduci, string[i])
        signi *= s
        #print("iiiiii stringi[%d] = %s" % (i, string[i]))
        #print("iiiiii (signi, reduci= = (%d, %s)" % (signi, reduci))

        (s, reducRighti) = divide(string[i], reducRighti)
        signRighti *= s

        #print("!!!!! signRighti, reducRighti) = (%d, %s)" % (signRighti, reducRighti))

        if signi != 1 or reduci != 'i': continue

        reducj = '1'
        signj = 1
        signRightj = signRighti
        reducRightj = reducRighti
        for j in range(i+1, len(string)-1):
            (s, reducj) = multiply(reducj, string[j])
            signj *= s
            #print("jjjjjjj stringj[%d] = %s" % (j, string[j]))
            #print("jjjjjjj (signj, reducj= = (%d, %s)" % (signj, reducj))

            (s, reducRightj) = divide(string[j], reducRightj)
            signRightj *= s
            #print("(kkkkkkk signRightj, reducRightj) = (%d, %s)" % (signRightj, reducRightj))

            if signj != 1 or reducj != 'j': continue

            reduck = reducRightj
            signk = signRightj

            #print("stringk: %s" % stringk)
            if signk == 1 and reduck == 'k':
                print("Case #%d: YES" % c)
                return

    print("Case #%d: NO" % c)




fname = "test.in"
cases = readFile(fname)
for c in range(len(cases)):
    solve(cases[c], c+1)
