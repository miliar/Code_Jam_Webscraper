import sys
def reduce(callable, iterable, ini=None):
    iterable = iter(iterable)

    ret = iterable.next() if ini is None else ini

    for item in iterable:
        ret = callable(ret, item)

    return ret


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def hcff(*args):
    """Return hcf of args."""   
    return reduce(gcd, args)

#####################

def printMove():
    tmp=raw_input()
    tmp=tmp.split()
    N=int(tmp[0])
    L=int(tmp[1])
    H=int(tmp[2])
    freq=raw_input()
    freq=freq.split()
    for i in xrange(len(freq)):
        freq[i]=int(freq[i])
        
    freq.sort()
   # print "N: ",N
   # print "L: ",L
   # print "H: ",H
   # print freq
    ##SORTED LIST DONE
    flag =0
    for f in xrange(L,H+1):
        for x in xrange(len(freq)):
            if freq[x] < f:
                if f % freq[x] is not 0:
                    flag =1
                    break
            if freq[x] > f:
                if  freq[x] % f is not 0:
                    flag =1
                    break
        if flag is 1:
            flag=0
            continue
        if flag is 0:
            print f
            return 0
            break
        
    print "NO"
        
    return 0

####################
sys.stdin = open("in.txt", "r")

sys.stdout = open("out.txt", "w")
no = input()
for i in xrange(0,no):
    print "Case #{0}:".format(i+1),
    printMove()

sys.stdout.close()
#
