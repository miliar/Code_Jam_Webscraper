from math import sqrt, ceil, floor
def c(filein,fileout):
    f = open(filein,'r')
    g = open(fileout,'w')
    count = int(f.readline()[:-1])
    for i in xrange(count):
        checkrange = f.readline().split(' ')
        count = 0
        for j in xrange(int(ceil(sqrt(int(checkrange[0])))),int(floor(sqrt(int(checkrange[1]))))+1):
            if isFairAndSquare(j):
                count+=1
        g.write("Case #"+str(i+1)+": "+str(count)+"\n")

def isPalindrome(x):
    s = str(x)
    for i in xrange(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def isFairAndSquare(x):
    return isPalindrome(x) and isPalindrome(x*x)
c('C-small-attempt0.in','csmall.out')
