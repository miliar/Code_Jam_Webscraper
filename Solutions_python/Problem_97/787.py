def recycledpairs(cas, A, B):
    """
    >>> recycledpairs(1, 1, 9)
    'Case #1: 0'
    >>> recycledpairs(2, 10, 40)
    'Case #2: 3'
    >>> recycledpairs(3, 100, 500)
    'Case #3: 156'
    >>> recycledpairs(4, 1111, 2222)
    'Case #4: 287'
    >>> recycledpairs(5, 1, 2000000)
    'Case #5: 2498454'
    """
    n = 0
    # 1 <= A <= B <= 2000000. 
    for x in range(A, B + 1):
        ca = str(x)
        ica = x
        len_ca = len(ca)
        appairable = []
        for i in range(1, len_ca):
            if ca[i] == '0':
                continue
            #cb = ca[i:].lstrip('0') + ca[:i]
            cb = ca[i:] + ca[:i]
            icb = int(cb)
            if icb > ica and icb <= B and len(cb) == len_ca and icb not in appairable:
                appairable.append(icb)
                #print '(%d, (%d) "%s", "%s") %d <= %d < %d <= %d' % (i, x, ca[i:], ca[:i], A, int(ca), int(cb), B)
                n += 1
        #print ca, bladbg    
    return 'Case #%d: %d' % (cas, n)
    
if __name__ == '__main__':
    import sys
    f = sys.stdin
    T = int(f.readline())
    for tc in range(1, T + 1):
        A, B = f.readline().strip('\n').split(' ')
        print recycledpairs(tc, int(A), int(B))
    #import doctest
    #doctest.testmod()   