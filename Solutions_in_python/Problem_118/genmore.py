from solve import ispalindrome
import sys

def digits(x):
    return len(str(x))

vals = []
maxdigits = 0
for line in open('nlist.txt'):
    num, sq = [int(v) for v in line.strip().split()]
    vals.append((num, sq))
    maxdigits = max(digits(num), maxdigits)

def add(v):
    n = int(v)
    assert ispalindrome(n)
    if ispalindrome(n * n):
        #print n
        vals.append((n, n * n))

def getseq(l):
    return [str(x[0]) for x in vals if digits(x[0]) == l]

def genval(count, i):
    #print "genval", count, i
    if i == 1:
        seq = ["0", "1", "2"]
    elif i == 2:
        seq = ["00", "11", "22"]
    else:
        seq = getseq(i)
    leftover = count - i
    assert leftover % 2 == 0
    d = leftover / 2
    for s in seq:
        yield "0" * d + s + "0" * d

def genrep1(c):
    if c % 2 == 1:
        for i in range(1, c+1, 2):
            for v in genval(c, i):
                yield v
    else:
        for i in range(2, c+1, 2):
            for v in genval(c, i):
                yield v

for i in range(maxdigits+1, 55):
    c = i - 2
    # 1 case
    for v in genrep1(c):
        d = "1" + v + "1"
        add(d)
    # 2 case
    d = "2" + "0" * (c) + "2"
    add(d)
    if c % 2 == 1:
        d = "2" + "0" * (c/2) + "1" + "0" * (c/2) + "2"
        add(d)

for a, b in vals:
    print a, b
