def rotate(n, A, B):
    lead_n = int([a for a in str(n)][0])
    lead_B = int([a for a in str(B)][0])
    x = [a for a in str(n)]
    for i in range(1, len(x)):
        lead = int(x[i])
        if lead == 0 or lead < lead_n or lead > lead_B:
            continue
        m = ''.join(x[i:] + x[:i])
        m = int(m)
        if A <= n < m <= B:
            yield m

def solve(A, B):
    res = 0
    if B < 10:
        return 0
    for n in range(A, B):
        x = [a for a in str(n)]
        if max(x[1:]) < x[0]:
            continue
        for m in rotate(n, A, B):
            if A <= n < m <= B:
                nx = [a for a in str(n)]
                mx = [a for a in str(m)]
                nxs = ''.join(nx)
                mxs = ''.join(mx + mx)
                mxss = mxs.replace(nxs, '.')
                x1 = mxss.split('.')
                x2 = x1[1] + x1[0]
                res += 1
#                print res, ':', A, n, m, B
#                print n, m, mxs, mxss, nxs, x2
                assert nxs in mxs
                assert x2 == nxs
    return res

def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    T = int(lines[0])
    for i in range(1, T+1):
        line = lines[i]
        
        line = line.strip()
        A, B = [int(t) for t in line.split()]
        res = solve(A, B)        
        
        print "Case #%d: %s" % (i, res)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
    