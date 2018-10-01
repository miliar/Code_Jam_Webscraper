
def main(input):
    from decimal import Decimal
    N = int(input.readline())
    for i in range(N):
        l = int(input.readline())
        n = Decimal(3)
        t = Decimal(1)
        s = []
        while l > 0:
            if (l & 1) != 0:
                s.append(1)
            else:
                s.append(0)
            l /= 2
        s.reverse()
        assert s[0]==1
        for b in s[1:]:
            n, t = n*n + 5*t*t, 2*n*t
            #print 'a', n, t
            if b:
                n, t = 3*n+5*t, 3*t+n
                #print 'b', n, t
        n+=(5*t*t).sqrt()
        n%=1000
        n=str(int(n))
        n = '0'*(3-len(n)) + n
        print "Case #%d:"%(i+1), n

if __name__ == '__main__':
    import sys
    f = sys.stdin
    #f = open('C.txt')
    main(f)
