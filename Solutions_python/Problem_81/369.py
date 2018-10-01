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
    N, = r(long)
    games = []
    W = []
    total = []
    WP = []
    OWP = []
    OOWP = []
    #print N, PD, PG
    for n in range(N):
        game, = r(str)
        win = 0
        tot = 0
        for k in range(N):
            if game[k] == '.':
                continue
            elif game[k] == '1':
                win += 1.0
            tot += 1.0
        games.append(game)
        W.append(win)
        total.append(tot)
        WP.append(win/tot)
    for n in range(N):
        owp = 0
        tot = 0
        for k in range(N):
            if games[n][k] == '.':
                continue
            elif games[n][k] == '1':
                owp += (W[k]/(total[k] - 1.0))
            else:
                owp += ((W[k] - 1)/(total[k] - 1.0))
            tot += 1
        OWP.append(owp/tot)
    for n in range(N):
        oowp = 0
        tot = 0
        for k in range(N):
            if games[n][k] == '.':
                continue
            else:
                oowp += OWP[k]
                tot += 1.0
        #print oowp,tot
        OOWP.append(oowp/tot)

    #print WP, OWP, OOWP
    print "Case #%d:"%(t+1)
    for n in range(N):
        print (0.25 * WP[n]) + (0.5 * OWP[n]) + (0.25 * OOWP[n])
    #print "Case #%d: %s %s"%(t+1, N, A, B)