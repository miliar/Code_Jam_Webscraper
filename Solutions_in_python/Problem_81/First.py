__author__ = 'Artur'

def getWP (m, i, j, N):
    sum = 0
    count = 0
    for k in range(0, N):
        if k != j and m[i][k] != -1:
            count += 1
            sum += m[i][k]
    return 1.0 * sum / count

input = open("in.in", 'r')


T = int ( input.readline() )

for t in range(1, T + 1):
    m = []
    N = int ( input.readline() )
    for i in range(0, N):
        m.append([])
        x = input.readline()
        for j in range(0, N):
            if x[j] == '.':
                m[i].append(-1)
            else:
                m[i].append( int ( x[j] ) )

    wp = []
    for i in range(0, N):
        wp.append( getWP(m, i, -1, N) )

    owp = []
    for i in range(0, N):
        count = 0
        sum = 0
        for j in range (0, N):
            if m[i][j] != -1:
                count += 1
                sum += getWP(m, j, i, N)
        owp.append( sum / count )

    oowp = []

    for i in range(0, N):
        count = len ( [ owp[j] for j in range(0, N) if m[i][j] != -1 ] )
        sum = reduce (lambda x, y: x+y, [ owp[j] for j in range(0, N) if m[i][j] != -1 ] )
        oowp.append( sum * 1.0 / count )

    res = []
    for i in range(0, N):
        res.append( 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] )

    print "Case #%d:" % t
    for rpi in res:
        print rpi