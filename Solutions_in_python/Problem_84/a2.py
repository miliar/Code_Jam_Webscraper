def check(m):
    for l in m:
        for c in l:
            if c == '#':
                return False
    return True

for case in xrange(input()):
    r, c = [int(x) for x in raw_input().split()]
    m = [[x for x in raw_input()] for i in xrange(r)]
    for i in xrange(r-1):
        for j in xrange(c-1):
            if m[i][j] == '#' and m[i][j+1] == '#' and m[i+1][j] == '#' and m[i+1][j+1] == '#':
                m[i][j] = '/'
                m[i][j+1] = '\\'
                m[i+1][j] = '\\'
                m[i+1][j+1] = '/'
    print "Case #%d:" % (case+1)
    if check(m): 
        print '\n'.join([''.join(l) for l in m])
    else:
        print 'Impossible'
