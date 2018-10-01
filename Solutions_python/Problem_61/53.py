
def check(lst, n):
    if n in lst:
        p = lst.index(n)
        if p == 0:
            return True
        return check(lst, p+1)
    else:
        return None
        
def count(n):
    cnt = 0
    for i in xrange(2**(n-2)):
        lst = [k+2 for k in range(n) if 1<<k & i]
        lst.append(n)
        #print lst, check(lst, n)
        if check(lst, n):
            cnt += 1
    return cnt

if __name__ == '__main__':
    #for n in range(2, 26):
    #    print n, count(n)    
    
    tbl =[0, 0, 1, 2, 3, 5, 8, 14, 24, 43
      , 77, 140, 256, 472, 874, 1628
      , 3045, 5719, 10780, 20388, 38674, 73562
      , 140268, 268066, 513350, 984911]
    
    T = int(raw_input())
    for t in range(T):
        n = int(raw_input())
        print "Case #%d: %d" % (t+1, tbl[n] % 100003)