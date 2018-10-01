import os, sys, math
from numpy import rate

#__debug=True
__debug=False

def debug(str):
    if __debug:
        print "[DEBUG] %s" % str

def main():
    no_cases=int(sys.stdin.readline().strip())
    for i in range(1,no_cases+1):
        variables=sys.stdin.readline().strip().split(' ')
        B=int(variables[0])
        N=int(variables[1])
        debug("B %d N %d"%(B,N))
        Mk=[int(m) for m in sys.stdin.readline().strip().split(' ')]
        debug("Mk %s"%Mk)
        m_lcm=lcmm(*Mk)
        debug("lcm %d"%m_lcm)
        barbers=[0]*B
        customer_one_round=sum(m_lcm/m for m in Mk)
        debug("customer_one_round %d"%customer_one_round)
        customer_left=N%customer_one_round
        debug("customer_left %d"%customer_left)
        if customer_left==0:
            customer_left=customer_one_round
        for j in range(0,customer_left):
            min_barber=min(barbers)
            barber_idx=barbers.index(min_barber)
            barbers[barber_idx]+=Mk[barber_idx]
            if j<50 or j==customer_left-1:
                debug("customer %d goes to %d: %s"% (j+1,barber_idx+1,barbers))
        print "Case #%d: %d" % (i, barber_idx+1)
    return 0

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

if __name__ == "__main__":
    main()
