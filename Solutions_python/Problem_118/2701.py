import math

def is_int(n):
    return n - int(n) == 0

def is_palindrome(n):
    # print "pal ", n
    s = str(n)
    l = len(s) - 1
    i = 0
    j = l
    # print len(s), i, j
    while i <= j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True


f = open('in', 'r')
num_cases = int(f.readline())


for ic in xrange(num_cases):
    out_str = "Case #%s:" % (ic + 1)
    line = f.readline()
    toks = line.split(' ')
    a = int(toks[0])
    b = int(toks[1])
    count = 0
    for n in xrange(a,b+1):
        if is_palindrome(n):
            m = math.sqrt(n)
            if is_int(m) and is_palindrome(int(m)):
                    count+=1
    out_str += " " + str(count)
    print out_str
