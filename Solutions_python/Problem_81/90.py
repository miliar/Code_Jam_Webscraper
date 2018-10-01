_case = 0
def gout(s):
    global _case
    _case += 1
    print "Case #%d: %s" % (_case,s) 

def memoize(f):
    dict = {}
    def func(*n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = f(*n)
            return dict[n]
    return func

for _ in xrange(int(raw_input())):
    wl = []
    for _ in xrange(int(raw_input())):
        wl.append(raw_input())
    wins = []
    losses = []
    
    for i,team in enumerate(wl):
        wins.append(0)
        losses.append(0)
        for game in team:
            if game == '1':
                wins[i] += 1
            if game == '0':
                losses[i] += 1
    
    wp = []
    owp = []
    oowp = []
    
    for i in xrange(len(wl)):
        wp.append(float(wins[i]) / float(wins[i] + losses[i]))
        totowp = 0
        for j,c in enumerate(wl[i]):
            if c != '.':
                totowp += float(wins[j] - (1 if c=='0' else 0)) / float(wins[j] + losses[j] - 1)
        owp.append(float(totowp) / float(wins[i] + losses[i]))
    
    rpi = []
    for i in xrange(len(wl)):
        totoowp = 0
        for j,c in enumerate(wl[i]):
            if c != '.':
                totoowp += owp[j]
        oowp.append(float(totoowp) / float(wins[i] + losses[i]))
        
        rpi.append('%.12f' % (.25*wp[i] + .5*owp[i] + .25*oowp[i]))
        
    gout('\n' + '\n'.join(rpi))
