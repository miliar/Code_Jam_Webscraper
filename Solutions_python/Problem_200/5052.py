
import sys

# Debug 
DEBUG = 0


# is n a tidy integer? 
def isTidy(n):
    sn = str(n)
    digits = [ int(c) for c in sn ]
    
    tidy = True

    while digits:
        
        # first vs. last
        d0 = digits[0]
        dN = digits[-1]

        if DEBUG: print "d0, DN ", d0, dN

        if d0 > dN:
            tidy = False
            break

        # Remove first and last
        del digits[0]
        if digits: del digits[-1]

        if not digits:
            break
        elif len(digits) == 1:
            if d0 > digits[0] or digits[0] > dN:
                tidy = False
                break

    return tidy


#
T = int(sys.stdin.readline())
if DEBUG: print "T=", T

for iT in range(T):
    
    N = int(sys.stdin.readline())
    if DEBUG: print "N=", N

    last_tidy_number = N
    for number in xrange(N, 0, -1):
        if isTidy(number):
            last_tidy_number = number
            break

    print "Case #{}: {}".format(iT+1, last_tidy_number)
