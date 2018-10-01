"""
Fair and Square
"""
import itertools
import math

def generate_palindromes(a,b):
    palindromes = []
    l = len(str(a))
    m = len(str(b))
    if(l==m and l==1):
        return list(xrange(a,b+1))
    for x in xrange(l,m+1):
        if(x==1):
            palindromes = list(xrange(a,10))
        elif(x%2==0):
            for y in xrange(int(10**(x/2-1)), int(10**(x/2))):
                rev = list(str(y))
                rev.reverse()
                candidate = int(str(y) + "".join(rev))
                if(candidate>=a):
                    if(candidate<=b):
                        palindromes.append(candidate)
                    else:
                        return palindromes  
        else:
            for y in xrange(int(10**(x/2)), int(10**(x/2+1))):
                rev = list(str(y))
                rev.reverse()
                candidate = int(str(y) + "".join(rev[1:]))
                if(candidate>=a):
                    if(candidate<=b):
                        palindromes.append(candidate)
                    else:
                        return palindromes  
                
    return palindromes

def check_palindrome(n):
    n_str = str(n)
    flag = True
    for i in xrange(int(math.ceil(len(n_str)/2.0))):
        if(n_str[i]!=n_str[-1*(i+1)]):
            flag = False
    return flag


f = open("input3.txt", "rb")
g = open("output3.txt", "wb")

t = int(f.readline().strip())

for i in xrange(t):
    a,b = map(int,f.readline().strip().split())
    palindromes = generate_palindromes(int(math.ceil(math.sqrt(a))), int(math.floor(math.sqrt(b))))
    count = 0
    for p in palindromes:
        if(check_palindrome(p**2)):
            count += 1
    g.write("Case #%d: %d" % (i+1, count))
    g.write("\n")