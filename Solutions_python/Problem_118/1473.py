import sys

def ispalindrome(p):
    s = str(p)
    for q in xrange(len(s)):
        if s[q] != s[len(s)-q-1]:
            return False
        if q > (len(s)/2):
            break
    return True

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for i in xrange(cases):
    caseval = 0
    candidate = 1
    j = 1
    ab = stdin[i].split()
    a = int(ab[0])
    b = int(ab[1])
    while candidate < a:
        candidate += 2*j
        candidate += 1
        j += 1
    while a <= candidate <= b:
        if ispalindrome(j) and ispalindrome(candidate):
            caseval += 1
        candidate += 2*j
        candidate += 1
        j += 1
    print "Case #"+str(i+1)+":", str(caseval)
