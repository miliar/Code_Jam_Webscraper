import fileinput
import fractions

infile = fileinput.input()

def r(fn='none', splt=True):
    '''r(fn=none, splt=True)
    Example: N, = r(long)
    r(str,splt=False)
    '''
    inp = infile.readline()
    if splt:
        inp = inp.split()
        return map(fn, inp)
    else:
        return fn(inp)

def t(st):
    k = st.split(':')
    return float(k[0]) + (float(k[1])/100.0)

T, = r(long)

for t in range(T):
    R, C = r(long)
    Tiles = []
    blue = 0
    
    #print N, PD, PG
    for x in range(R):
        row, = r(str)
        Tiles.append(row)
    impossible = False
    for x in range(R):
        for c in range(C):
            if Tiles[x][c] == '#':
                if (x+1 < R and c+1 < C) and Tiles[x+1][c] == '#' and Tiles[x][c+1] == '#' and Tiles[x+1][c+1] == '#':
                    #print "Before", Tiles
                    Tiles[x] = Tiles[x][:c] + '/\\' + Tiles[x][c+2:]
                    Tiles[x+1] = Tiles[x+1][:c] + '\/' + Tiles[x+1][c+2:]
                    #print "After", Tiles
                else:
                    impossible = True
                    break
            if impossible:
                break
    print "Case #%d:"%(t+1)
    #print WP, OWP, OOWP
    if impossible:
        print "Impossible"
    else:
        for row in Tiles:
            print row
    #for n in range(N):
    #    print (0.25 * WP[n]) + (0.5 * OWP[n]) + (0.25 * OOWP[n])
    #print "Case #%d: %s %s"%(t+1, N, A, B)