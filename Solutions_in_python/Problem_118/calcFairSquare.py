from math import *



def isPal(n):
    s = str(n)
    splitted = list(s)
    l = len(splitted)
    for i in xrange(l):
        if splitted[i] != splitted[l-1-i]:
            return False
    return True



def countSuperFair(binf, bsup):
    
    pinf = int(ceil(sqrt(binf)))
    psup = int(floor(sqrt(bsup)))        
#    
    nsuperfair = 0
    superfair = []    
    
    for i in xrange(pinf, psup+1):
        if not isPal(i): continue
        sq = i*i
        if isPal(sq):
            nsuperfair +=1
#             print i,sq
#             superfair.append((i,sq))
#     print superfair    
    return nsuperfair

    
        
# def fastPalGenerator(i, j):
#     digitsi = len(list(str(i)))
#     digitsj = len(list(str(j)))
    

    
    
def fastPalGenerator(ndigits):
    if ndigits == 0: yield 0
    if ndigits == 1:
        for i in xrange(10):
            yield i
    if ndigits>=2:
        for n in range(1, 10):
            for n2  in fastPalGenerator(ndigits-2):
               r = n*(10**(ndigits-1)) + n + n2*10
               yield r

               
def fastPalGenerator2(ndigits):
    if ndigits == 0: yield 0
    if ndigits == 1:
        for i in xrange(3):
            yield i
    if ndigits>=2:
        for n in range(0, 3):
            for n2  in fastPalGenerator2(ndigits-2):
               r = n*(10**(ndigits-1)) + n + n2*10
               yield r
               
def M(n):
    for i in fastPalGenerator2(n):
        if isPal(i*i):
            print i, i**2
               
    
    
def fastPalAB(a, b):
    from itertools import chain
    
    digitsA = len(str(a))
    digitsB = len(str(b))
    
    iterators =[]
    
    for d in xrange(digitsA, digitsB+1):
        iterators.append(fastPalGenerator(d))
    c = chain(*iterators)
    
    for i in c:
        if i>a and i<b:
            yield i
    
    
    
if __name__ == "__main__":
    f = open("input", 'r')
    nprobs = int(f.readline())
    
    for i in xrange(nprobs):
        line = f.readline()
        lspl = line.split()
        binf = int(lspl[0])
        bsup = int(lspl[1])
        
        print "Case #%i: %i"%(i+1, countSuperFair(binf, bsup))
        
        