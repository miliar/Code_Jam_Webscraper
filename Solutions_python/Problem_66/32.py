USE_PSYCHO = True
#USE_PSYCHO = False

if USE_PSYCHO:
    import psyco
    psyco.full()


from numpy import *

def solve2(M,Prices, X, P, P2):
    if P == 0:
        if M[2*X] == 0 or M[2*X+1] == 0:
            return Prices[0][X]
        else:
            return 0
    noSkip = Prices[P][X] + solve2(M,Prices,2*X, P-1, P2 / 2) + solve2(M,Prices,2*X+1, P-1, P2 / 2)

    canSkip = True
    A = X* P2
    B = A + P2
    for x in M[A:B]:
        if x == 0:
            canSkip = False
            break

    if canSkip:
        for i in xrange(A,B):
            M[i] -= 1
        possible = solve2(M,Prices,2*X, P-1, P2 / 2) + solve2(M,Prices,2*X+1, P-1, P2 / 2)
        for i in xrange(A,B):
            M[i] += 1
        return min(possible, noSkip)
    else:
        return noSkip
        

def solve(filecontent):
    lines = filecontent.splitlines()
    T = int(lines[0])
    out = []
    lines = lines[1:]
    for tcase in xrange(1,T+1):
        # DEBUG PRINT
        print "tcase is ",tcase
        line1 = lines[0].split(" ")
        P, = map(int,line1)
        lines = lines[1:]
        
        M = array(map(int, lines[0].split(" ")))
        lines = lines[1:]

        Prices = [array(map(int, x.split(" "))) for x in lines[:P]]
        lines = lines[P:]

        res = str(solve2(M,Prices,0, P-1, 2**P))
        
        tcaseOut = ("Case #%d: %s" % (tcase,res))
        out.append(tcaseOut)
    return "\n".join(out)

def main(letter, isSmall, suffix):
    if isSmall:
        sizeStr = "small"
    else:
        sizeStr = "large"
    fname = "codejam/%s-%s%s.in" % (letter, sizeStr, suffix)
    
    f = file(fname).read()
    #print solve(f)
    file("codejam/this.out",'w').write(solve(f))

main("B",False,"")
