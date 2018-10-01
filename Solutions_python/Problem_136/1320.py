def getint():
    return int(raw_input())
    
def getlist():
    return [float(x) for x in raw_input().split()]
    
def fun(c, f, x, r):
    a = x/r
    rc = False
    if c < x:
        a1 = c/r
        a2 = x/(r+f)
        if (a1+a2) < a:
            a = a1
            rc = True
    return a, rc

def test(n):
    C, F, X = getlist()
    rate = 2.0
    t = 0
    rc = True
    while rc:
        _t, rc = fun(C, F, X, rate)
        t += _t
        rate += F
        
    print 'Case #%d: %.7f'%(n, t)

def main():
    T = getint()
    for i in range(T):
        test(i+1)

if __name__ == '__main__':
    main()