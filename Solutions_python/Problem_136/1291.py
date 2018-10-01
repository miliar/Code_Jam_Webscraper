import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        c, ff, x = f.readline().strip().split()
        c = float(c)
        ff = float(ff)
        x = float(x)
        
        rate = 2.0
        elapsed = 0.0
        while True:
            farmtime = c / rate
            
            newfarm = elapsed + farmtime + x / (rate + ff)
            nonewfarm = elapsed + x / rate
            
            #print rate, elapsed, farmtime, newfarm, nonewfarm
            if nonewfarm <= newfarm:
                elapsed = nonewfarm
                break
            else:
                elapsed += farmtime
                rate = rate + ff
                
        print "Case #%d: %f" % (caseno+1, elapsed)
        
main()