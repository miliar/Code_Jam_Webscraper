import sys

def is_palindrome(a):
    s = str(a)
    lens = len(s)
    for i in range(0, lens/2+1):
        if (s[i] != s[-i-1]):
            return False
    return True

# for large 2 input
sqpal = [ 1, 4,  9, ]
nlist = [ 22, 11]
# nlist = [ 101, 111, 121, 202, 212 ]
l3 = 10**100
n = nlist.pop()
while n**2 <= l3: # in nlist:
    sqpal.append(n**2)
    s = str(n)
    lens = len(s)
    if lens % 2 == 0:
        for i in (0, 1, 2):
            newn = long(s[:lens/2] + str(i) + s[lens/2:])
            if (is_palindrome(newn**2) and is_palindrome(newn)):
                nlist.insert(0, newn)
                # print newn, newn**2

    else:
        newn = long(s[:lens/2+1] + s[lens/2:])
        if (is_palindrome(newn**2) and is_palindrome(newn)):
            nlist.insert(0, newn)
            # print newn, newn**2
            # sqpal.append(newn**2)

    n = nlist.pop()
#    print newn

#for n in sqpal:
    #print n
# print sqpal
# print len(sqpal)

line = sys.stdin.readline()
T = int(line.rstrip())
for t in range(0, T):
    line = sys.stdin.readline()
    a, b = line.rstrip().split()
    a, b = long(a), long(b)
    sol = 0
    for i in sqpal:
        if (a <= i and i <= b):
            sol += 1
        if (i > b):
            break
    print 'Case #%d: %d' % (t+1, sol)
