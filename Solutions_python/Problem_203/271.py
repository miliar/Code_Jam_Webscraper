if __name__=="__main__":
    ncases = int(raw_input())
    for t in xrange(1, ncases+1):
        r,c = [int(s) for s in raw_input().split()]
        g = []
        for x in range(r):
            g.append(list(raw_input().strip()))

        for row in g:
            for col in xrange(c-1):
                if row[col+1] == '?' and row[col] !='?':
                    row[col+1] = row[col]
            for col in reversed(xrange(1,c)):
                if row[col-1] == '?' and row[col] != '?':
                    row[col-1] = row[col]


                            
        # Smear down
        for row in xrange(r-1):
            if g[row+1][0] == '?' and g[row][0] != '?':
                g[row+1] = g[row]

        # Smear up
        for row in reversed(xrange(1,r)):
            if g[row-1][0] == '?' and g[row][0] != '?':
                g[row-1] = g[row]

        print "Case #{}:".format(t)
        for row in g:
            print ''.join(row)





