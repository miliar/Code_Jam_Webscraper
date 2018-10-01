#!/usr/env/bin python
import math

def shorten(q,p):
    may_short = True

    while(may_short):
        may_short = False
        inv_quot = p/float(q)
        if inv_quot == int(inv_quot) and inv_quot != 0:
            q /= inv_quot
            p /= inv_quot
            may_short = True
        print q, p
    return q, p

if __name__ == "__main__":
    infile = open("./data/A-small-attempt4.in", 'r')
    outfile = open("./data/A-small-attempt4.out", 'w')
    n = int(infile.readline())
    for c in xrange(n):
        p, q = [int(x) for x in infile.readline().split("/")]

        q, p = shorten(q, p)
        quot = q/float(p)
        found_it = False
        gen = 0
        l = math.log(q, 2)
        possible = True
        if l != int(l):
            n_gen = "impossible"
        else:
            for x in xrange(41):
                den = 2<<x
                if quot <= den:
                    found_it = True
                    gen = x+1
                    break

            if found_it:
                n_gen = gen
        # quot_2 = int(q/float(p)*2)
        # if quot%2 != 0 and quot_2%2 !=0: 
        #     n_gen = "impossible"
        # else:
        #     n_gen = int(math.log(quot, 2))
        
        # print n_gen
        outfile.write("Case #{cn}: {answer}\n".format(cn=c+1, answer=n_gen))
