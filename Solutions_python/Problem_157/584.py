__author__ = 'bszikszai'

from io import *

lookup = {
    ('1','1'): '1',
    ('1','i'): 'i',
    ('1','j'): 'j',
    ('1','k'): 'k',
    ('i','1'): 'i',
    ('i','i'): '-1',
    ('i','j'): 'k',
    ('i','k'): '-j',
    ('j','1'): 'j',
    ('j','i'): '-k',
    ('j','j'): '-1',
    ('j','k'): 'i',
    ('k','1'): 'k',
    ('k','i'): 'j',
    ('k','j'): '-i',
    ('k','k'): '-1',
          }
def multiply_(a, b):
    return lookup[(a,b)]

def multiply(a, b):
    isneg = False
    if(a.startswith('-')):
        a = a[1:]
        isneg = not isneg
    if(b.startswith('-')):
        b = b[1:]
        isneg = not isneg
    res = lookup[(a, b)]
    if(res.startswith('-')):
        res = res[1:]
        isneg = not isneg
    return res if not isneg else '-'+res

def reduce(s):
    res = '1'
    for c in list(s):
        res = multiply(res, c)
    return res

def solve(t):
    #print t
    resLeft = ['1']
    resRight = ['1']
    prev = '1'
    for x in range(0, len(t)):
        prev = multiply(prev, t[x])
        resLeft.append(prev)
    prev = '1'
    for x in range(len(t)-1, -1, -1):
        prev = multiply(t[x], prev)
        resRight.append(prev)
    resRight.reverse()
    #print resLeft
    #print resRight
    for x in range(0, len(t)):
        if(resLeft[x] == 'i' and resRight[x] == 'i'):
            print x
            for y in range(x+1, len(t)):
                if (resLeft[y] == 'k' and resRight[y] == 'k'):
                    print y
                    return 'YES'
            return 'NO'
    return 'NO'

def testcase(f):
    rep = int(f.readline().split(' ')[1])
    raw = f.readline().rstrip('\n').rstrip('\r')
    print "Starting solve"
    return solve(raw*rep)

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = testcase(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))